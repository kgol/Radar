from tkinter import *
from tkinter import simpledialog
'''g_color=""
g_width=800
g_height=600'''
class Dialog(simpledialog.Dialog):
    def body(self, master):
        Label(master, text="width:").grid(row=0)
        Label(master, text="height:").grid(row=1)
        self.button = Button(master, text="save", fg="red", command=self.save).grid(row=2,sticky=W)

        self.e1=Entry(master)
        self.e2=Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1
    def save(self):
        accesslist=[str(self.e1.get()),str(self.e2.get())]
        accessout=open("accesslist.txt",'w')
        for item in accesslist:
            accessout.write(item)
            accessout.write('\n')
        accessout.close()
    
    def apply(self):
        width = int(self.e1.get())
        height = int(self.e2.get())
        print(width, height)

class Window:
    def __init__(self, master):
        frame = Frame(master)
        frame.grid(row=0,sticky=W)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit).grid(row=1,sticky=W)
        self.button = Button(frame, text="Dimension", fg="BLUE", command=self.dialog).grid(row=2,sticky=W)
        self.button = Button(frame, text="Color", fg="green", command=self.color).grid(row=3,sticky=W)
        self.button = Button(frame, text="Check", fg="purple", command=self.check).grid(row=4,sticky=W)


    def dialog(self):
        dialog=Dialog(root)
    def color(self):
        slave=Tk()
        def black():
            global color_1
            color_1="black"
            print("You chose "+color_1)
        def white():
            global color_1
            color_1="white"
            print("You chose "+color_1)
        def yellow():
            global color_1
            color_1="yellow"
            print("You chose "+color_1)
        def save():
            acces_1="accesslist.txt"
            with open(acces_1) as f:
                lines = f.read().splitlines()
            print(lines)
            lines.pop(2)
            lines.append(color_1)
            print(lines)
            with open(acces_1,'w') as acces:
                for item in lines:
                    acces.write(item)
                    acces.write('\n')
                acces.close()
        def quit():
            slave.quit()
        Button(slave, text="black", fg="white", bg="black", command=black).grid(row=1,sticky=W)
        Button(slave, text="white", fg="black", bg="white", command=white).grid(row=2,sticky=W)
        Button(slave, text="yellow", fg="black", bg="yellow", command=yellow).grid(row=3,sticky=W)
        Button(slave, text="save", fg="red", command=save).grid(row=4,sticky=W)
        #Button(slave, text="quit", fg="red", command=quit).grid(row=4,sticky=W)
    def check(self):
        accessin=open("accesslist.txt",'r')
        print(accessin.read())
        
root = Tk()
window = Window(root)

root.mainloop()
