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
        self.photo = PhotoImage(file='images/' + self.name + '.gif')
        self.theta = theta*pi/180
        if(self.parent != None): #C'est pas le Soleil
            self.x = self.parent.x + convertDist(self.dist)*cos(self.theta)
            self.y = self.parent.y + convertDist(self.dist)*sin(self.theta)
            self.speedX = -cos(pi/2-getAngle(self, self.parent))*speed
            self.speedY = -sin(pi/2-getAngle(self, self.parent))*speed

    def move(self, delta):
        G = getG()
        if self.parent != None: #La planète bouge, ce n'est pas le Soleil
            self.speedX = self.accelX*delta + self.speedX
            self.speedY = self.accelY*delta + self.speedY
            self.x = convertDist(self.speedX*delta*1e-3) + self.x
            self.y = convertDist(self.speedY*delta*1e-3) + self.y
            # pixels=convertDist(self.dist)
            # self.theta = sqrt(G*self.parent.mass/((self.dist*10**3)**3))*delta + self.theta
            # self.x = -pixels*sin(self.theta) + self.parent.x
            # self.y = pixels*cos(self.theta) + self.parent.y
        else : #Déplacement du Soleil
            factor = 10**-5
            self.x = self.x + getSpeedScrollX()*delta*factor
            self.y = self.y + getSpeedScrollY()*delta*factor

    """Renvoie la projection sur x et y de la force d'attraction exercée par la planète sur un autre objet"""
    def attract(self, xObj, yObj, massObj, theta):
        G = getG()
        force = G*massObj*self.mass/(invConvertDist(getDistance(xObj, self.x, yObj, self.y))*10**3)**2
        attractX = force*cos(theta)
        attractY = -force*sin(theta)
        return [attractX, attractY]
