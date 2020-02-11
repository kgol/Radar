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
        root = Tk()

        Colors =[
                ("Black","B"),
                ("White","W"),
                ("Yellow","Y")
                ]

        v = StringVar()
        v.set("B")

        for text, color in Colors:
            b = Radiobutton(root, text=text, variable=v, value=color)
            b.pack(anchor=W)

        root.mainloop()
        
        print("Selected color:"+text)
        
    def dim(self):
        dialog=Dialog(root)

root = Tk()
app = App(root)

root.mainloop()
root.destroy() # optional; see description below