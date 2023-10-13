from tkinter import *
from tkinter import filedialog as fd

# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        # adding or using askopenfilename method from filedialog module.
        name = fd.askopenfilename()
        load = Image.open(name)
        # load = Image.open('C:\\Users\\chukwunonso.molokwu\\Desktop\\Python_practice\\gui programming with tkinter\\tree_sunset.jpg')
        render = ImageTk.PhotoImage(load)
        img = Label(self,image=render)
        img.image = render
        img.place(x=0,y=0)

root = Tk()
app = Window(root)
root.wm_title("Images")
root.geometry("200x120")
root.mainloop()