import os
import sys

# Import des bibliothèques nécessaires
import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

import constants  # Fichier contenant les constantes, comme l'API Key

# Configuration de la clé API OpenAI
os.environ["OPENAI_API_KEY"] = constants.APIKEY

# Activer PERSIST pour enregistrer sur le disque et réutiliser le modèle
PERSIST = False

# Récupération de l'argument de ligne de commande, s'il existe
query = None
if len(sys.argv) > 1:
    query = sys.argv[1]

# Charger l'index à partir du disque si PERSIST est activé
if PERSIST and os.path.exists("persist"):
    print("Réutilisation de l'index...\n")
    vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
    index = VectorStoreIndexWrapper(vectorstore=vectorstore)
else:
    # Charger les données à partir du fichier "politiqueconges.txt"
    ##loader = TextLoader("data/politiqueconges.txt")  # Utilisez cette ligne si vous avez seulement besoin de data.txt
    loader = DirectoryLoader("data/")  # Utilisez cette ligne pour charger un répertoire de documents
    if PERSIST:
        index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory": "persist"}).from_loaders([loader])
    else:
        index = VectorstoreIndexCreator().from_loaders([loader])

# Création d'une chaîne de recherche et de réponse conversationnelle
chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

# Historique de conversation
chat_history = []

# Boucle principale d'interaction avec l'utilisateur
while True:
    if not query:
        query = input("Prompt: ")  # Demande de l'entrée utilisateur
    if query in ['quit', 'q', 'exit']:
        sys.exit()  # Quitter le programme si l'utilisateur entre "quit", "q" ou "exit"
    result = chain({"question": query, "chat_history": chat_history})  # Obtenir une réponse de la chaîne
    print(result['answer'])  # Afficher la réponse au sein de la conversation

    # Ajouter l'échange à l'historique de conversation
    chat_history.append((query, result['answer']))
    query = None  # Réinitialisation de la requête pour la prochaine itération
