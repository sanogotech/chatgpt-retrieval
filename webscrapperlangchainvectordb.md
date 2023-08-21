

# How to use LangChain with OpenAI, Pinecone, and Apify

- https://blog.apify.com/how-to-use-langchain/


# Use LangChain, Pinecone, and Apify to extend the capabilities of OpenAI's ChatGPT and answer questions based on data after 2021 or from any dataset.


OpenAI’s ChatGPT has rapidly evolved into a very powerful and versatile tool. People have been using it to generate text, answer questions, translate languages, and much more. Trained on data up to September 2021, a big ChatGPT limitation is its inability to answer questions based on more recent information. So, how can we use OpenAI to create a system that can answer questions from current data? Several tools, including LangChain, Pinecone, and Apify, offer the ability to extend and enhance the capabilities of OpenAI's AI models.

* LangChain: 

a framework designed for the development of applications that leverage language models. It allows us to integrate large language models like OpenAI and Hugging Face with different applications.

* Pinecone: an external tool that allows us to save the embeddings online and extract them whenever we need.

* Apify: 

a web scraping and automation platform that significantly streamlines the process of data collection. It provides the capability to scrape data and subsequently feed it to LLMs. This allows us to train LLMs on real-time data and develop applications.
In this tutorial, we will extract data using one of Apify’s many pre-built web scraping tools, Airbnb Scraper. We'll scrape Airbnb data from New York City and feed it to the LLM to make a system that will answer questions from that data.

## How to set up LangChain and Apify

```
mkdir LangChain
cd LangChain
touch main.ipynb
```

```
pip3 install langchain==0.0.189 pinecone-client openai tiktoken nest_asyncio apify-client chromadb
```

```
pip freeze | egrep '(langchain|pinecone-client|openai|tiktoken|nest_asyncio|apify-client|chromadb)'
```

## Python code

```python

import os
# Add your OPENAI API key below
os.environ["OPENAI_API_KEY"] = ""
# Add your APIFY API key below
os.environ["APIFY_API_TOKEN"] = ""






```