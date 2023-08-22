# chatgpt-retrieval

Simple script to use ChatGPT on your own files.

Here's the [YouTube Video](https://youtu.be/9AXP7tCI9PI).

![AI  Full 360](https://github.com/sanogotech/chatgpt-retrieval/blob/main/images/AIfullcompenent.jpg)

## Docs

- https://www.melvinvivas.com/chatgpt-openai-natural-language-to-api-call

- https://www.davidgentile.net/langchain-indexes-document-loaders/

- https://www.geeksforgeeks.org/python-downloading-captions-from-youtube/

- https://www.linkedin.com/pulse/transforming-question-answering-openai-langchain-harnessing-routu/

- https://blog.nextideatech.com/chat-with-documents-using-langchain-gpt-4-python/

##   Le modèle GPT-3.5-turbo de OpenAI est utilisé pour générer des réponses, sans pour autant inclure de nouvelles données.


Je comprends que vous souhaitez savoir comment vous pouvez utiliser l'indexation du fichier politiqueconges.txt pour ajouter vos propres données à OpenAI. Cependant, d'après le code que vous avez fourni, il semble que le fichier politiqueconges.txt est utilisé pour créer un index local à l'aide de la bibliothèque langchain, mais le modèle GPT-3.5-turbo de OpenAI est utilisé pour générer des réponses, sans pour autant inclure de nouvelles données.

Malheureusement, à ma connaissance, GPT-3.5-turbo ne prend pas en charge le fine-tuning traditionnel avec de nouvelles données comme un modèle classique. Il est pré-entrainé par OpenAI et ne peut être affiné qu'en utilisant des "prompt engineering", c'est-à-dire en formulant bien les instructions et en fournissant des exemples pertinents.

Si vous voulez ajouter vos propres données et que celles-ci doivent être prises en compte par GPT-3.5-turbo, vous devez les intégrer dans vos exemples et instructions. Voici comment vous pourriez le faire :

Exemples d'entraînement : Vous pouvez inclure vos propres exemples pertinents dans les instructions que vous fournissez au modèle. Par exemple, si vous utilisez GPT-3.5-turbo pour répondre à des questions sur la politique de congé, incluez des exemples spécifiques de questions sur la politique de congé dans vos instructions.

Instructions détaillées : Fournissez des instructions détaillées sur la manière dont vous souhaitez que le modèle réponde aux questions basées sur les données que vous souhaitez intégrer. Plus vous serez spécifique dans vos instructions, plus le modèle sera capable de générer des réponses pertinentes.

Variation des exemples : Utilisez une variété d'exemples pour couvrir différents aspects des données que vous souhaitez intégrer. Cela peut aider le modèle à généraliser et à fournir des réponses pertinentes à un large éventail de questions.

En résumé, bien que vous ne puissiez pas ajouter directement de nouvelles données au modèle GPT-3.5-turbo, vous pouvez façonner les instructions et les exemples que vous fournissez pour que le modèle génère des réponses en tenant compte de vos propres données et scénarios. N'oubliez pas de suivre les meilleures pratiques de formulation d'instructions pour obtenir des résultats optimaux.

## Using Langchain and Open Source Vector DB Chroma for Semantic Search with OpenAI's LLM

* https://github.com/PradipNichite/Youtube-Tutorials/blob/main/Chroma_DB_with_Langchain.ipynb

* https://blog.futuresmart.ai/using-langchain-and-open-source-vector-db-chroma-for-semantic-search-with-openais-llm
  
  ```
  pip install  openai langchain sentence_transformers chromadb unstructured -q
   ```

Creating Vector Store with Chroma DB
Vector stores serve as a prevalent method for handling and searching through unstructured data. The standard process involves creating embeddings from the unstructured data, saving these generated vectors, and then, during a query, embedding the unstructured query to retrieve the 'most similar' vectors to this embedded query. The role of a vector store is primarily to facilitate this storage of embedded data and execute the similarity search.

Importantly, Langchain offers support for various vector stores, including Chroma, Pinecone, and others. This flexibility enables users to choose the most suitable vector store based on their specific requirements and preferences.

Let's create a vector store using the Chroma DB from the documents we loaded and split.


  ```
from langchain.vectorstores import Chroma
db = Chroma.from_documents(docs, embeddings)
  ```

## Vector Database

* https://dev.to/josethz00/vector-databases-5df1
  
With the rise of AI, vector databases are becoming more popular. But what exactly is a vector database and when should you use it?

* What is a vector database?
Traditional search engines use full-text search, but NLPs like ChatGPT and Bing AI use semantic search or similarity search, a type of search that considers not only the characters match, but also the meaning of the words. This feature of semantic search is powered by vector databases.

 Recently Google also started using semantic search
 

* Full-text search VS Semantic search
Let's compare these two types of search.

- Full-text search
Search for a word or phrase in large amounts of text
The search engine returns a list of documents that contain the search term

```
SELECT title, content
FROM documents
WHERE search_vector @@ plainto_tsquery('english', 'example search');

```

- Semantic search
Search for a word or phrase in large amounts of text
The search engine will return a list of documents that contain the search term or have a similar meaning.

*  Ocean // Sea (mimilar meaning)
  
How the vector database knows which vectors are similar?

Querying the database using math formulas to find the closest vectors in a high-dimensional space

* Euclidean distance
* Cosine similarity

* Machine learning algorithms

  - K-nearest neighbors (KNN)
  - Approximate nearest neighbors (ANN)
  -
* Indexing
## Installation

```
python --version
Python 3.9.13
```

* Install C and C++ support in Visual Studio

* https://learn.microsoft.com/en-us/cpp/build/vscpp-step-0-installation?view=msvc-170

Install [Langchain](https://github.com/hwchase17/langchain) and other required packages.
```
pip install langchain openai chromadb tiktoken unstructured
```
Modify `constants.py.default` to use your own [OpenAI API key](https://platform.openai.com/account/api-keys), and rename it to `constants.py`.

Place your own data into `data/data.txt`.

## Example usage
Test reading `data/data.txt` file.
```
> python chatgpt.py "what is my dog's name"
Your dog's name is Sunny.
```

Test reading `data/cat.pdf` file.
```
> python chatgpt.py "what is my cat's name"
Your cat's name is Muffy.
```
