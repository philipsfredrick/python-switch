# pip install gTTS
from gtts import gTTS
import os

myText = "Hello World"

language = "en"

myObj = gTTS(text=myText, lang=language, slow=False)
myObj.save("voice.mp3")
os.system("mediaplayer voice.mp3")

"""
1. Integrate wikipedia with gTTS. What's searched on wiki will be spoken out as speech.
2. 
"""