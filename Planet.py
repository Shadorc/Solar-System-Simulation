from math import *
from Maths import *
from tkinter import *

class Planet():

    def __init__(self, parent, name, mass, diam, dist, speed, theta):
        self.parent = parent
        self.name = name
        self.mass = mass
        self.diam = diam
        self.dist = dist
        self.speed = speed
        self.accel = 0
        self.theta = theta*pi/180
        self.photo = PhotoImage(file='images/' + self.name + '.gif')
        if(self.parent != None): #Ce n'est pas le Soleil
            self.x = convKmToPixel(self.dist)*cos(self.theta) + self.parent.x
            self.y = convKmToPixel(self.dist)*sin(self.theta) + self.parent.y
            self.speedX = -cos(pi/2-getAngle(self, self.parent))*speed
            self.speedY = -sin(pi/2-getAngle(self, self.parent))*speed

    def move(self, delta):
        G = getG()
        self.speedX = self.accelX*delta + self.speedX + getSpeedScrollX()
        self.speedY = self.accelY*delta + self.speedY + getSpeedScrollY()
        self.x = convKmToPixel(self.speedX*delta*1e-3) + self.x
        self.y = convKmToPixel(self.speedY*delta*1e-3) + self.y

    """Renvoie la projection sur x et y de la force d'attraction exercée par la planète sur un autre objet"""
    def attract(self, xObj, yObj, massObj, theta):
        G = getG()
        #Convertis la distance pixels<->km puis km<->m
        d = convPixelToKm(getDistance(xObj, self.x, yObj, self.y))*10**3
        force = (G*massObj*self.mass)/(d**2)
        attractX = force*cos(theta)
        attractY = -force*sin(theta)
        return [attractX, attractY]
