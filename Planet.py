from math import *
from Maths import *
from tkinter import *

class Planet():

    def __init__(self, parent, name, mass, diam, dist, theta):
        self.parent = parent
        self.name = name
        self.mass = mass
        self.diam = diam
        self.dist = dist
        self.photo = PhotoImage(file='images/' + self.name + '.gif')
        self.theta = theta
        if(self.parent != None): #C'est pas le Soleil
            self.x = self.parent.x + self.dist
            self.y = self.parent.y
        
    def move(self, delta):
        """Décrit les trajectoires des planètes"""
        G = 6.67e-11
        if self.parent != None: #La planète bouge
            pixels=convertDist(self.dist)
            self.theta = sqrt(G*self.parent.mass/((self.dist*10**3)**3))*delta + self.theta
            self.x = -pixels*sin(self.theta) + self.parent.x
            self.y = pixels*cos(self.theta) + self.parent.y
        else : #Déplacement du Soleil
            self.x = self.x + getSpeedX()
            self.y = self.y + getSpeedY()
