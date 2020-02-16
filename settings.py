from tkinter import *
from tkinter import simpledialog
from radar3 import radar as radar
import colors


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
        accesslist=[]
        acces_1="accesslist.txt"
        with open(acces_1) as f:
                lines = f.read().splitlines()
        
        accessout=open("accesslist.txt",'w')
        if (self.e1.get() != ""):
            width = self.e1.get()
            accessout.write(str(width))
            accessout.write('\n')
        else:
            accessout.write(lines[0])
            accessout.write('\n')
       
        if (self.e2.get() != ""):
            height=self.e2.get()
            accessout.write(str(height))
            accessout.write('\n')
        else:
            accessout.write(lines[1])
            accessout.write('\n')
        if len(lines)<3:
            accessout.write("black")
        else:
            accessout.write(lines[2])
            accessout.write('\n')
       # accesslist=[str(width),str(height),'black']
        #accessout=open("accesslist.txt",'w')
        #for item in accesslist:
          #  accessout.write(item)
        #    accessout.write('\n')
        accessout.close()
    
    def apply(self):
        #width = int(self.e1.get())
        #height = int(self.e2.get())
        #print(width, height)
        return

class Window:
    def __init__(self, master):
        frame = Frame(master)
        frame.grid(row=0,sticky=W)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit).grid(row=1,sticky=W)
        self.button = Button(frame, text="Dimension", fg="BLUE", command=self.dialog).grid(row=2,sticky=W)
        self.button = Button(frame, text="Color", fg="green", command=self.color).grid(row=3,sticky=W)
        self.button = Button(frame, text="Check", fg="purple", command=self.check).grid(row=4,sticky=W)
        self.button = Button(frame, text="START", fg="black", bg="green", command=self.start).grid(row=5,sticky=E)

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
        def fajny():
            global color_1
            color_1 = "fajny"
            print("You chose "+color_1)
        def save():
            acces_1="accesslist.txt"
            with open(acces_1) as f:
                lines = f.read().splitlines()
            print(lines)
            #lines.pop(2)
            lines[2]=color_1
            print(lines)
            with open(acces_1,'w') as acces:
                for item in lines:
                    acces.write(item)
                    acces.write('\n')
                acces.close()
        def dupa():
            slave.destroy()
        Button(slave, text="black", fg="white", bg="black", command=black).grid(row=1,sticky=W)
        Button(slave, text="white", fg="black", bg="white", command=white).grid(row=2,sticky=W)
        Button(slave, text="yellow", fg="black", bg="yellow", command=yellow).grid(row=3,sticky=W)
        Button(slave, text="fajny", fg="black", bg="blue", command=fajny).grid(row=4,sticky=W)
        Button(slave, text="save", fg="red", command=save).grid(row=5,sticky=W)
        Button(slave, text="quit", fg="red", command=dupa).grid(row=6,sticky=W)
    def check(self):
        accessin=open("accesslist.txt",'r')
        print(accessin.read())
    def start(self):
        acces_1="accesslist.txt"
        with open(acces_1) as f:
                lines_1 = f.read().splitlines()
        if lines_1[2] == "black":
            color = colors.black
        elif lines_1[2] == "white":
            color = colors.white
        elif lines_1[2] == "yellow":
            color = colors.yellow
        elif lines_1[2] == "fajny":
            color = colors.fajny
        start=radar(int(lines_1[0]), int(lines_1[1]), color)
        
root = Tk()
window = Window(root)

root.mainloop()
