
# pip install youtube-transcript-api
# pip install pytube

from langchain.document_loaders import YoutubeLoader

loader = YoutubeLoader.from_youtube_url("https://www.youtube.com/watch?v=i70wkxmumAw", add_video_info=True)

transcript_document = loader.load()


print("La transcription de la vidéo ", "https://www.youtube.com/watch?v=i70wkxmumAw", transcript_document)