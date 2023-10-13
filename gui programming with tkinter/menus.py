from tkinter import *

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        menu = Menu(self.master)
        self.master.config(menu = menu)
        self.pack(fill=BOTH,expand=1)
        text = Label(self,text="Nonso")
        text.place(x=70,y=90)
        # text.pack()
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit",command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)
        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=editMenu)
    
    def exitProgram(self):
        exit()
       
# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("Python Window")
root.geometry('320x200')
# show window
root.mainloop()