from tkinter import *
from Maths import *
from KeyListener import *

class Frame():
    
    def __init__(self):
        self.frame = Tk()
        self.frameW = self.frame.winfo_screenwidth()
        self.frameH = self.frame.winfo_screenheight()
        self.frame.title("Simulateur Système Solaire V0.1")
        self.univers = Canvas(self.frame, width=self.frameW, height=self.frameH)
        self.univers.configure(background='black')
        self.univers.focus_set()
        self.univers.bind("<KeyPress>",keyPressed)
        self.univers.bind("<KeyRelease>",keyReleased)
        self.univers.pack()

        self.v = StringVar()
        self.timer = Label(self.frame, textvariable=self.v, bg='black', fg='white')
        self.timer.pack()

    def draw(self, obj):
        self.univers.create_image(obj.x, obj.y, image=obj.photo, anchor=CENTER)

    def setTime(self, elapsed):
        self.v.set(round(elapsed/31536000))
