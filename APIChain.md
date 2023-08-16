
#  APIChain

## Docs

- https://www.melvinvivas.com/chatgpt-openai-natural-language-to-api-call

- https://www.davidgentile.net/langchain-indexes-document-loaders/

- https://www.linkedin.com/pulse/transforming-question-answering-openai-langchain-harnessing-routu/

- https://blog.nextideatech.com/chat-with-documents-using-langchain-gpt-4-python/

- https://blog.bytebytego.com/p/how-to-build-a-smart-chatbot-in-10


## LangChain

Prompts: This module allows you to build dynamic prompts using templates. It can adapt to different LLM types depending on the context window size and input variables used as context, such as conversation history, search results, previous answers, and more.

Models: This module provides an abstraction layer to connect to most available third- party LLM APIs. It has API connections to ~40 public LLMs, chat and embedding models.

Memory: This gives the LLMs access to the conversation history.

Indexes: Indexes refer to ways to structure documents so that LLMs can best interact with them. This module contains utility functions for working with documents and integration to different vector databases.

Agents: Some applications require not just a predetermined chain of calls to LLMs or other tools, but potentially to an unknown chain that depends on the user’s input. In these types of chains, there is an agent with access to a suite of tools. Depending on the user’s input, the agent can decide which – if any – tool to call.

Chains: Using an LLM in isolation is fine for some simple applications, but many more complex ones require the chaining of LLMs, either with each other, or other experts. LangChain provides a standard interface for Chains, as well as some common implementations of chains for ease of use.

## OneMap API Endpoint

We would use LangChain’s APIChain function to translate the user’s query for the street address and postal code of OurTampines Hub into an API call to the OneMap API.

The OneMap API would then return the desired information, which LangChain would process and return to the user in a natural language format. For instance, LangChain might respond with “The street address of Our Tampines Hub is “1 TAMPINES WALK OUR TAMPINES HUB SINGAPORE 528523”.

The result of the API is a JSON object. We can then use the JSON object to retrieve the desired information and return it to the user in a natural language format. This will be done automatically by LangChain.

OneMap API Endpoint

```
GET https://developers.onemap.sg/commonapi/search?searchVal=our%tampines%hub&returnGeom=N&getAddrDetails=Y&pageNum=1
```

** Response **

```
{
    "found": 1,
    "totalNumPages": 1,
    "pageNum": 1,
    "totalNumEntries": 1,
    "results": [
        {
            "SEARCHVAL": "OUR TAMPINES HUB",
            "BLK_NO": "1",
            "ROAD_NAME": "TAMPINES WALK",
            "BUILDING": "OUR TAMPINES HUB",
            "ADDRESS": "1 TAMPINES WALK OUR TAMPINES HUB SINGAPORE 528523",
            "POSTAL": "528523"
        }
]
}

```

##  API integration code sample

```python

import os

from langchain.chains import APIChain
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = ""

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", max_tokens=256, verbose=True)

apiSpec = """API documentation:
Base URL: https://developers.onemap.sg/commonapi
Endpoint: /search
Example API call: https://developers.onemap.sg/commonapi/search?searchVal=520201&returnGeom=Y&getAddrDetails=Y&pageNum=1

This API is for retrieving address details based on a search keyword.

Request POST payload (JSON object) 
Json Field	Format	Required	Default	Description
searchVal	String	No		Any string representing a steet address, establishment, location or postal code
returnGeom String Yes N always set to N
getAddrDetails String Yes Y always set to Y

INSTRUCTIONS FOR RESPONDING
Reply to the user with the first ADDRESS result, respond in natural language indicate the ADDRESS from the APi response. If data is empty, just say you the search has not returned any results and you are sorry.

"""

# set the headers if you need to do add authorization, for this example we don't need it because the API is public
# apiToken = ""
# headers = {"Authorization": f"Bearer {apiToken}"} 
# chain_new = APIChain.from_llm_and_api_docs(llm, apiSpec, verbose=True, headers=headers)

chain_new = APIChain.from_llm_and_api_docs(llm, apiSpec, verbose=True)
response = chain_new.run('What is the postal code of Our Tampines Hub?')

```
print(response)