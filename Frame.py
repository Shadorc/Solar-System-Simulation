from tkinter import *
from Maths import *
from KeyListener import *

class Frame():
    
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Simulateur Système Solaire V0.1")
        self.frameW = self.frame.winfo_screenwidth()
        self.frameH = self.frame.winfo_screenheight()
        
        p = PanedWindow(self.frame, orient=VERTICAL)
        p.pack( expand=1, fill=BOTH)
        
        self.textCoords = StringVar()
        self.labelCoords = Label(p, textvariable=self.textCoords, background='White', anchor=CENTER)
        p.add(self.labelCoords)
        
        self.univers = Canvas(p, width=self.frameW, height=self.frameH)
        self.univers.configure(background='black')
        self.univers.focus_set()
        self.univers.bind("<KeyPress>",keyPressed)
        self.univers.bind("<KeyRelease>",keyReleased)
        self.univers.bind("<Button-1>", mouseClicked)
        self.univers.pack()
        p.add(self.univers)

    def createPopup(self, list):
        top = Toplevel()
        top.title("A propos de "+ str(list[0]))

        msg = Message(top, text=list)
        msg.pack()

        button = Button(top, text="Fermer", command=top.destroy)
        button.pack()

    def draw(self, obj):
        self.univers.create_image(obj.x, obj.y, image=obj.photo, anchor=CENTER)

    def setInfos(self, x, y, elapsed):
        self.textCoords.set('Coordonnées X:' + str(self.frameW/2-x) + " Y:" 
        + str(y-self.frameH/2) + "\nTemps: " + str(round(elapsed)))
