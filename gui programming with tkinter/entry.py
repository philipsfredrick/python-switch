import tkinter as tk

window = tk.Tk()
window.title("Enter Inputs")
window.geometry("500x300")

e1 = tk.Entry(window,show=None,font=("Arial",14))
e2 = tk.Entry(window,show='*',font=("Arial",14))

e1.pack()
e2.pack()

window.mainloop()

# from tkinter import *

# top = Tk()
# L1 = Label(top,text="Label")
# L1.pack(side=LEFT)
# E1 = Entry(top, bd=5)
# E1.pack(side=LEFT)

# top.mainloop()