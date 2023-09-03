"""
* https://www.geeksforgeeks.org/python-convert-image-to-text-and-then-to-speech/
* https://linuxhint.com/install-tesseract-windows/

Our goal is to convert a given text image into a string of text, saving it to a file and to hear what is written in the image through audio.

For this, we need to import some Libraries

Pytesseract(Python-tesseract) : It is an optical character recognition (OCR) tool for python sponsored by google.
pyttsx3 : It is an offline cross-platform Text-to-Speech library
Python Imaging Library (PIL) : It adds image processing capabilities to your Python interpreter
Googletrans : It is a free python library that implements the Google Translate API.

pip install googletrans==3.1.0a0
* https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group

pip install pyttsx3
pip install pytesseract
"""

# import the following libraries
# will convert the image to text string
import pytesseract	

# adds image processing capabilities
from PIL import Image	

# converts the text to speech
import pyttsx3		

#translates into the mentioned language
from googletrans import Translator	

# opening an image from the source path
img = Image.open('image2.png')	

# describes image format in the output
print(img)						
# path where the tesseract module is installed
#pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
pytesseract.pytesseract.tesseract_cmd ='C:/Users/SOULEYSANOGO/AppData/Local/Tesseract-OCR/tesseract.exe'
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)
# write text in a text file and save it to source path
with open('abc.txt',mode ='w') as file:	
	
				file.write(result)
				print(result)
				
p = Translator()					
# translates the text into german language
k = p.translate(result,dest='german')	
print(k)
engine = pyttsx3.init()

# an audio will be played which speaks the test if pyttsx3 recognizes it
engine.say(k)							
engine.runAndWait()

