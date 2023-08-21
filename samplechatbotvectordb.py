# https://blog.bytebytego.com/p/how-to-build-a-smart-chatbot-in-10?utm_source=profile&utm_medium=reader2
# pip install pinecone-client langchain openai wikipedia google-api-python-client unstructured tabulate pdf2image
# /p/how-to-build-a-smart-chatbot-in-10?utm_source=profile&utm_medium=reader2
#  Google alphabet doc:  https://abc.xyz/investor/earnings/

import os

from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter

import pinecone 
from langchain.vectorstores import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings

from langchain import OpenAI
from langchain.chains import RetrievalQA

# let’s get some data

loader = DirectoryLoader(
    './Langchain/data/', # my local directory
    glob='**/*.pdf',     # we only get pdfs
    show_progress=True
)
docs = loader.load()
print(docs)


# We split them into chunks. 
text_splitter = CharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=0
)
docs_split = text_splitter.split_documents(docs)
print(docs_split)


#Each chunk corresponds to an embedding vector.
#For this reason, we need to convert the data into embeddings and store them in a database.
# Pinecone: A vector database

# To store the data, I use Pinecone. You can create a free account and automatically get API keys with which to access the database

# Before continuing, make sure to get a OpenAI API key by signing up to the OpenAI


PINECONE_API_KEY = ... # find at app.pinecone.io
PINECONE_ENV = ...     # next to api key in console
OPENAI_API_KEY = ...   # found at platform.openai.com/account/api-keys

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# We upload the data to the vector database. The default OpenAI embedding model used in Langchain is 'text-embedding-ada-002' (OpenAI embedding models.) It is used to convert data into embedding vectors



# we use the openAI embedding model
embeddings = OpenAIEmbeddings()
pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)

doc_db = Pinecone.from_documents(
    docs_split, 
    embeddings, 
    index_name='langchain-demo'
)

# We can now search for relevant documents in that database using the cosine similarity metric

query = "What were the most important events for Google in 2021?"
search_docs = doc_db.similarity_search(query)
print(search_docs)


# Retrieving data with ChatGPT
# We can now use a LLM to utilize the database data. Let’s get an LLM such as GPT-3
llm = OpenAI()

qa = RetrievalQA.from_chain_type(
    llm=llm, 
    chain_type='stuff',
    retriever=doc_db.as_retriever(),
)

query = "What were the earnings in 2022?"
result = qa.run(query)

print(result)

"""
> 'The total revenues for the full year 2022 were $282,836 million, with operating income and operating margin information not provided in the given context.'

"""