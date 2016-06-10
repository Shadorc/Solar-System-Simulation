from tkinter import *
from Maths import *
from KeyListener import *

class Frame():
    
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Simulateur Système Solaire V0.3")
        
        self.frameW = self.frame.winfo_screenwidth()
        self.frameH = self.frame.winfo_screenheight()

        #Curseur modifiant la vitesse d'écoulement du temps
        self.time=DoubleVar()
        timeScale = Scale(self.frame, from_=-12, to=12, orient=HORIZONTAL, variable=self.time, length=200, sliderlength=20, label='mois/sec')
        timeScale.set(1)
        timeScale.pack()
        
        panel = PanedWindow(self.frame, orient=VERTICAL)
        panel.pack(expand=1, fill=BOTH)

        #Label affichant les coordonnées
        self.textCoords = StringVar()
        self.labelCoords = Label(panel, textvariable=self.textCoords, background='White', anchor=CENTER)
        panel.add(self.labelCoords)

        #Canvas représentant l'Univers
        self.univers = Canvas(panel, width=self.frameW, height=self.frameH)
        self.univers.configure(background='black')
        self.univers.bind("<KeyPress>", keyPressed)
        self.univers.bind("<Button-1>", mouseClicked)
        self.univers.pack()
        self.univers.focus_set()
        panel.add(self.univers)

    def createPopup(self, list):
        top = Toplevel()
        top.title("A propos de " + str(list[0]))
        top.geometry("300x120+200+200") #width x height + x + y

        infos = ("Masse : "+str(list[1])+" kg"
        "\nDiamètre : " + str(list[2]) + " km"
        "\nDistance par rapport au Soleil : " + str(list[3]) + " km"
        "\nTempérature : " + str(list[4]) + " K"
        "\nPériode de révolution : " + str(list[5]).replace('\n', '') + " jours")
        label = Label(top, text=infos, height=0, width=150)
        label.pack()
        
        button = Button(top, text="Fermer", command=top.destroy)
        button.pack()

    def draw(self, obj):
        self.univers.create_image(obj.x, obj.y, image=obj.photo, anchor=CENTER)

    #Modifie les infos dans l'en-tête
    def setInfos(self, x, y, elapsed):
        self.textCoords.set('Coordonnées du vaisseau X:' + str(self.frameW/2-x) + " Y:" + str(y-self.frameH/2)
                            + "\nTemps: " + str(round(elapsed/31536000)) + "ans")
