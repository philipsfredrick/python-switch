# pip install wikipedia
from gtts import gTTS
import os
import wikipedia
import tkinter as tk

window = tk.Tk()
window.title("Enter Inputs")
window.geometry("500x300")

e1 = tk.Entry(window,show=None,font=("Arial",14))
e1.pack()

def search():
    myText = e1.get()
    result = wikipedia.summary(myText, sentences = 5)
    language = "en"
    myObj = gTTS(text=result, lang=language, slow=False)
    myObj.save("assign.mp3")
    os.system("mediaplayer assign.mp3")
    e1.delete(0, tk.END)

def user_input():
    button = tk.Button(window, text="Search Wiki", command=search)

    search.pack()

user_input()
window.mainloop()
# myText = input("Please enter your search text here: ")

# printing result
# print(result)



