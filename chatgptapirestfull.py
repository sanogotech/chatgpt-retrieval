# pip install fastapi uvicorn
# uvicorn main:app --reload

# uvicorn chatgptapirestfull:app --reload

"""
Accès à la documentation Swagger : Ouvrez votre navigateur et accédez à l'adresse
 http://127.0.0.1:8000/docs. Vous verrez la documentation Swagger générée 
 
 """
 

import os
import sys
from fastapi import FastAPI, Query
from pydantic import BaseModel
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.vectorstores import Chroma

# Importez les constantes depuis le fichier constants.py
from constants import APIKEY

app = FastAPI()

# Configuration de la clé API OpenAI
os.environ["OPENAI_API_KEY"] = APIKEY

# Charger les données à partir du fichier "politiqueconges.txt"
loader = TextLoader("data/politiqueconges.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

# Création d'une chaîne de recherche et de réponse conversationnelle
chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

# Historique de conversation
chat_history = []

# Modèle Pydantic pour la requête d'entrée
class QueryInput(BaseModel):
    question: str

# Définition de l'endpoint pour l'API
@app.post("/get_answer/")
async def get_answer(input_data: QueryInput):
    query = input_data.question
    result = chain({"question": query, "chat_history": chat_history})
    response = {
        "question": query,
        "answer": result['answer']
    }
    chat_history.append((query, result['answer']))
    return response
