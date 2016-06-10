from tkinter import *
from Maths import *
from KeyListener import *
from Point import *

class Frame():
    
    def __init__(self):
        self.frame = Tk()
        self.frame.title("Simulateur Système Solaire V0.3")
        
        self.frameW = self.frame.winfo_screenwidth()
        self.frameH = self.frame.winfo_screenheight()
        
        panel = PanedWindow(self.frame, orient=HORIZONTAL)
        panel.pack(expand=1)
        
        panelOptions = PanedWindow(panel, orient=VERTICAL, width=200)
        panelOptions.pack(expand=1, fill=BOTH)

        #Label affichant les coordonnées
        self.textInfos = StringVar()
        self.labelCoords = Label(panelOptions, textvariable=self.textInfos, background='White', anchor=CENTER)
        panelOptions.add(self.labelCoords)

        #Curseur modifiant la vitesse d'écoulement du temps
        self.time=DoubleVar()
        timeScale = Scale(panelOptions, from_=0, to=12, orient=HORIZONTAL, variable=self.time, sliderlength=20, label='mois/sec')
        timeScale.set(1)
        timeScale.pack()
        panelOptions.add(timeScale)
        
        #Curseur modifiant G
        self.g=StringVar()
        self.g.set(str(6.67e-11))
        gInput = Entry(panelOptions, textvariable=self.g, width=100)
        gInput.pack()
        panelOptions.add(gInput)
        
        gInputButton = Button(panelOptions, text="OK", command=self.valid)
        gInputButton.pack()
        panelOptions.add(gInputButton)
        
        self.showTrace = IntVar()
        checkBu = Checkbutton(panelOptions, text="Afficher la trace", variable=self.showTrace)
        checkBu.pack()
        panelOptions.add(checkBu)
        
        panel.add(panelOptions)

        #Canvas représentant l'Univers
        self.univers = Canvas(panel, width=self.frameW, height=self.frameH)
        self.univers.configure(background='black')
        self.univers.bind("<KeyPress>", keyPressed)
        self.univers.bind("<Button-1>", mouseClicked)
        self.univers.pack()
        self.univers.focus_set()
        panel.add(self.univers)
        
    def valid(self):
        setG(float(self.g.get()))
        self.univers.focus_set()

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
        
    def drawPoint(self, pt):
        self.univers.create_oval(pt.x-1, pt.y-1, pt.x+1, pt.y+1, fill='white')

    #Modifie les infos dans l'en-tête
    def setInfos(self, x, y, elapsed):
        self.textInfos.set('Coordonnées du vaisseau\nX:' + str(self.frameW/2-x) + " Y:" + str(y-self.frameH/2)
                            + "\n\nTemps: " + str(round(elapsed/31536000)) + "ans")
