from tkinter import *

root = Tk()

textLabel = Label(root, text="My Cheese Ball", justify=LEFT,padx=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file="\cheese.jpg")
imgLabel = Label(root,image=photo)
imgLabel.pack(side=RIGHT)

root.mainloop()