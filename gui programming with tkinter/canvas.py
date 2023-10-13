import tkinter

# init tk
root = tkinter.Tk()

# create canvas
myCanvas = tkinter.Canvas(root,bg="white",height=300,width=300)

# draw arcs
coord = 10, 10, 300, 300
arc1 = myCanvas.create_arc(coord,start=0,extent=150,fill="red")
arc2 = myCanvas.create_arc(coord,start=150,extent=180,fill="green")

# draw a line
line = myCanvas.create_line(10,10,100,100)
# add to window and show
myCanvas.pack()
root.mainloop()

# common drawing methods for canvas
# 1. Creating an oval - oval = C.create_oval(x0,y0,x1,y1,options)
# 2. Creating an arc - arc = C.create_arc(20,50,190,240,start=0,extent=110,fill="red")
# 3. Creating a line - line = C.create_line(x0,y0,x1,y1,...,xn,yn,options)
# 4. Creating a polygon - polygon = C.create_polygon(x0,y0,x1,y1,...,xn,yn,options)