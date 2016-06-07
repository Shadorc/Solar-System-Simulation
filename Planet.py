from math import *
from Maths import *
from tkinter import *
from KeyListener import *

class Planet():
    
    def __init__(self, parent, name, mass, diam, dist):
        self.name = name
        self.parent = parent
        self.dist = convertDist(dist)
        if(parent != None): #C'est pas le Soleil
            self.x = self.parent.x + self.dist
            self.y = self.parent.y
        self.photo = PhotoImage(file='images/' + self.name + '.gif')
        self.mass = mass
        self.diam = convertDist(diam)
        self.theta = 0
        
    def move(self, delta):
        G = 6.67e-11
        if self.parent != None: #La planète bouge
            distM = invConvertDist(self.dist)*10**3 #Reconvertit la distance en km puis en m
            self.theta = sqrt(G*self.parent.mass/distM**3)*delta + self.theta
            self.x = -self.dist*sin(self.theta) + self.parent.x
            self.y = self.dist*cos(self.theta) + self.parent.y
        else : #Déplacement du Soleil
            self.x = self.x + getX()
            self.y = self.y + getY()

