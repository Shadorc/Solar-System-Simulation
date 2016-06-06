from math import *
from Maths import *
from tkinter import *

class Planet():
    
    def __init__(self, parent, nameImg, mass, diam, dist):
        self.parent = parent
        self.dist = convertDist(dist)
        if(parent == None): #C'est le Soleil
            self.x = 500
            self.y = 300
        else:
            self.x = self.parent.x + self.dist
            self.y = self.parent.y
        self.photo = PhotoImage(file=nameImg)
        self.mass = mass
        self.diam = convertDist(diam)
        self.theta = 0
        
    def move(self, delta):
        G = 6.67*10**-25
        if self.parent != None: #La planète bouge
            self.theta = sqrt(G*self.parent.mass/(self.dist)**3)*delta + self.theta
            self.x = -self.dist*sin(self.theta) + self.parent.x
            self.y = self.dist*cos(self.theta) + self.parent.y

