from math import *
from Maths import *
from tkinter import *
from KeyListener import *

class Planet():

    def __init__(self, parent, name, mass, diam, dist, speed, theta):
        self.parent = parent
        self.name = name
        self.mass = mass
        self.diam = diam
        self.dist = dist
        self.speed = speed
        self.accel = 0
        self.theta = theta*pi/180 #On convertit les degrés en radians
        self.photo = PhotoImage(file='images/' + self.name + '.gif')
        if self.parent != None: #Ce n'est pas le Soleil
            self.x = convMeterToPixel(self.dist)*cos(self.theta) + self.parent.x
            self.y = convMeterToPixel(self.dist)*sin(self.theta) + self.parent.y
            self.speedX = -cos(pi/2-getAngle(self, self.parent))*self.speed + self.parent.speedX
            self.speedY = -sin(pi/2-getAngle(self, self.parent))*self.speed + self.parent.speedY

    def move(self, delta):
        G = getG()
        self.speedX = self.accelX*delta + self.speedX
        self.speedY = self.accelY*delta + self.speedY
        self.x = convMeterToPixel(self.speedX*delta + getSpeedScrollX()*delta) + self.x
        self.y = convMeterToPixel(self.speedY*delta + getSpeedScrollY()*delta) + self.y

    def attract(self, xObj, yObj, massObj, theta):
        """Renvoie la projection sur x et y de la force d'attraction exercée par la planète sur un autre objet sous forme de liste"""
        G = getG()
        d = convPixelToMeter(getDistance(xObj, self.x, yObj, self.y))
        force = (G*massObj*self.mass)/(d**2)
        accel = force/massObj
        attractX = accel*cos(theta)
        attractY = -accel*sin(theta)
        return [attractX, attractY]
