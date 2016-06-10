from math import *
from Maths import *
from tkinter import *
#from PIL import Image, ImageTk

class Planet():

    def __init__(self, parent, name, mass, diam, dist, theta):
        self.parent = parent
        self.name = name
        self.mass = mass
        self.diam = diam
        self.dist = dist
        self.photo = PhotoImage(file='images/' + self.name + '.gif')
        # image = Image.open('images/' + self.name + '.gif')
        # image = image.resize((ceil(convertDist(self.diam)),ceil(convertDist(self.diam))), Image.ANTIALIAS)
        # self.photo = ImageTk.PhotoImage(image)
        self.theta = theta
        if(self.parent != None): #C'est pas le Soleil
            self.x = self.parent.x + self.dist
            self.y = self.parent.y
            # image = Image.open('images/' + self.name + '.gif')
            # image = image.resize((ceil(convertDist(self.diam)),ceil(convertDist(self.diam))), Image.ANTIALIAS)
            # self.photo = ImageTk.PhotoImage(image)

    def move(self, delta):
        G = 6.67e-11
        if self.parent != None: #La planète bouge, ce n'est pas le Soleil
            pixels=convertDist(self.dist)
            self.theta = sqrt(G*self.parent.mass/((self.dist*10**3)**3))*delta + self.theta
            self.x = -pixels*sin(self.theta) + self.parent.x
            self.y = pixels*cos(self.theta) + self.parent.y
        else : #Déplacement du Soleil
            factor = 10**-5
            self.x = self.x + getSpeedScrollX()*delta*factor
            self.y = self.y + getSpeedScrollY()*delta*factor
        # image = Image.open('images/' + self.name + '.gif')
        # image = image.resize((ceil(convertDist(self.diam)),ceil(convertDist(self.diam))), Image.ANTIALIAS)
        # self.photo = ImageTk.PhotoImage(image)

    """Renvoie la projection sur x et y de la force d'attraction exercée par la planète sur un autre objet"""
    def attract(self, xObj, yObj, massObj, theta):
        G = 6.67e-11
        force = G*massObj*self.mass/(invConvertDist(getDistance(xObj, self.x, yObj, self.y))*10**3)**2
        attractX = force*cos(theta)
        attractY = -force*sin(theta)
        return [attractX, attractY]
