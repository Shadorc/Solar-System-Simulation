from math import *
from Maths import *
from tkinter import *
from KeyListener import *

class Planet():
    
    def __init__(self, parent, name, mass, diam, dist):
        self.parent = parent
        self.name = name
        self.mass = mass
        self.diam = convertDist(diam)
        self.dist = convertDist(dist)
        self.photo = PhotoImage(file='images/' + self.name + '.gif')
        self.theta = 0
        if(self.parent != None): #C'est pas le Soleil
            self.x = self.parent.x + self.dist
            self.y = self.parent.y
        
    def move(self, delta):
        G = 6.67e-11
        if self.parent != None: #La planète bouge
            distM = invConvertDist(self.dist)*10**3 #Reconvertit la distance en km puis en m
            self.theta = sqrt(G*self.parent.mass/distM**3)*delta + self.theta
            self.x = -self.dist*sin(self.theta) + self.parent.x
            self.y = self.dist*cos(self.theta) + self.parent.y
        else : #Déplacement du Soleil
            self.x = self.x + getSpeedX()*delta
            self.y = self.y + getSpeedY()*delta

