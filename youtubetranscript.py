# https://www.davidgentile.net/langchain-indexes-document-loaders/
# https://python.langchain.com/docs/integrations/document_loaders/youtube_transcript
# pip install youtube-transcript-api
# pip install pytube

from langchain.document_loaders import YoutubeLoader

urlvideoyoutube = "https://youtu.be/TiUtiPiRsXU"

loader = YoutubeLoader.from_youtube_url(urlvideoyoutube, add_video_info=True, language=["en", "fr"], translation="fr")



transcript_document = loader.load()


print("La transcription de la vidéo ", urlvideoyoutube, transcript_document)



"""

Transcription de la vidéo "Introduction à l'Innovation et à l'Entrepreneuriat"

Bonjour à tous, je me présente, moi Dominique Amener, je suis professeur permanente au 5/10. J'enseigne des matières comme l'innovation, l'entrepreneuriat, ou encore la RSE. Bienvenue à ce cours qui sera dédié à l'innovation et à l'entrepreneuriat, deux disciplines qui, à première vue, paraissent complètement différentes et indépendantes. Pourtant, elles sont totalement complémentaires. L'innovation peut intervenir avant le lancement d'un projet d'entreprise, pendant le lancement et la conception de ce projet, et même pour la gestion de l'entreprise. C'est une discipline transverse qui touche tous les domaines d'activité de la stratégie de l'entreprise ainsi que tous les départements opérationnels. C'est pourquoi nous les relions.

Je vais commencer par une petite caricature qui peut sembler anodine, mais qui en réalité illustre complètement l'approche des idées innovantes. Vous avez un monsieur qui essaie d'aider les autres à travers des roues, mais les autres ne font pas autant d'efforts que lui, malgré le temps de travail et l'énergie investis. Cela s'explique par leur zone de confort, les habitudes quotidiennes auxquelles ils s'accrochent, même s'ils savent que le changement leur serait bénéfique. C'est ce qu'on appelle la réticence au changement. Pour y remédier, il y a un mot clé important : la persévérance.

Si l'on observe les entrepreneurs à succès, on constate qu'ils ont toujours cru en leurs idées et qu'ils ont persévéré pour atteindre leur objectif. Ils sont visionnaires et ont des innovations majeures. Aujourd'hui, l'innovation est le moteur de l'économie, non seulement sur le plan économique, mais aussi pour les comportements humains. Des innovations comme les réseaux sociaux, Google, les smartphones, les PC sont devenus indispensables dans nos vies.

Certaines entreprises, appelées "licornes", ont une valorisation boursière très élevée. Cela montre que la puissance économique est liée à la possession des dernières innovations. L'évolution des comportements montre que l'adoption de l'innovation se fait de plus en plus rapidement. Les licornes sont principalement américaines et chinoises, montrant ainsi l'importance de l'innovation dans l'économie.

La quatrième révolution industrielle est en cours, centrée sur la robotique et l'intelligence artificielle. Les machines imitent les fonctions cognitives humaines, prennent des décisions basées sur des algorithmes mathématiques et sont capables de simuler l'intelligence humaine. L'intelligence artificielle se développe rapidement dans de nombreux domaines, y compris la relation client, l'industrie, l'agriculture, etc.

De nouveaux modèles économiques émergent, comme Airbnb, le B2C (business to consumer) remplaçant le B2B (business to business), les modèles d'abonnement, etc. Tout est en train de se digitaliser, des services web avancés à l'e-commerce en passant par l'e-learning et les transports.

En conclusion, l'innovation est au cœur de l'économie et des comportements actuels. La quatrième révolution industrielle, basée sur la robotique et l'intelligence artificielle, transforme de nombreux secteurs. Les nouveaux modèles économiques et la digitalisation sont au cœur de cette évolution.

Merci pour votre attention et à bientôt pour la prochaine vidéo sur les fondements de l'innovation.

"""