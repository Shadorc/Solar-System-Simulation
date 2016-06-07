from tkinter import *
from Maths import *

class Frame():
    
    def __init__(self):
        self.frameW = 1000
        self.frameH = 650
        self.frame = Tk()
        self.frame.title("Simulateur Système Solaire V0.1")
        self.univers = Canvas(self.frame, width=self.frameW, height=self.frameH)
        self.univers.configure(background='black')
        self.univers.pack() 

    def draw(self, obj):
        self.univers.create_image(obj.x, obj.y, image=obj.photo, anchor=CENTER)
    
