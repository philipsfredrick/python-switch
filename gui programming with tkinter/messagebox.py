import tkinter
import tkinter.messagebox

def buttonClick():
    # tkinter.messagebox.showinfo("title", "message")
    # tkinter.messagebox.showwarning("warn", "WARNING!!!!!")
    tkinter.messagebox.showerror("error", "An error has occurred!")

root=tkinter.Tk()
root.title("GUI for messagebox")
root.geometry("300x100")
root.resizable(False,False)
tkinter.Button(root,text="Hello button",command=buttonClick).pack()
root.mainloop()