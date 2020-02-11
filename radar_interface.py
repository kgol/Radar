import tkinter as tk
from tkinter import *
from tkinter import simpledialog

class Dialog(simpledialog.Dialog):
    def body(self, master):
        Label(master, text="width:").grid(row=0)
        Label(master, text="height:").grid(row=1)
        
        self.e1=Entry(master)
        self.e2=Entry(master)
        
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1
    def apply(self):
        width = int(self.e1.get())
        height = int(self.e2.get())
        print(width, height)

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        self.color = Button(frame, text="Colors", command=self.color)
        self.color.pack(side=LEFT)
        
        self.dim = Button(frame, text="Dimension", fg="blue", command=self.dim)
        self.dim.pack(side=LEFT)

    def color(self):
        def sel():
            selection = "You selected the option " + str(var.get())
            label.config(text = selection)

        var = IntVar()
        R1 = Radiobutton(root, text="Black", variable=var, value=1,
                  command=sel)
        R1.pack( anchor = W )

        R2 = Radiobutton(root, text="White", variable=var, value=2,
                  command=sel)
        R2.pack( anchor = W )

        R3 = Radiobutton(root, text="Option 3", variable=var, value=3,
                  command=sel)
        R3.pack( anchor = W)

        label = Label(root)
        label.pack()
   
    def dim(self):
        dialog=Dialog(root)

root = Tk()
app = App(root)

root.mainloop()
root.destroy() # optional; see description below