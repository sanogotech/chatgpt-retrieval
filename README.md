# chatgpt-retrieval

Simple script to use ChatGPT on your own files.

Here's the [YouTube Video](https://youtu.be/9AXP7tCI9PI).

![AI  Full 360](https://github.com/sanogotech/chatgpt-retrieval/blob/main/images/AIfullcompenent.jpg)

## Docs

- https://www.melvinvivas.com/chatgpt-openai-natural-language-to-api-call

- https://www.davidgentile.net/langchain-indexes-document-loaders/

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

## Installation

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
