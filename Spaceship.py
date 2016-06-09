from tkinter import *
from KeyListener import *

class Spaceship():
    
    def __init__(self, x, y):
        self.speedX = 0
        self.speedY = 0
        self.accelX = 0
        self.accelY = 0
        self.mass = 1000
        self.x = x
        self.y = y
        self.photo = PhotoImage(file="images/Spaceship_up.gif")

    def move(self, delta) :
        """Permet de gérer l'affichage du vaisseau selon sons sens de déplacement"""
        factor = 10**-5
        
        self.speedX = getSpeedSpaceX() + self.accelX*delta
        self.speedY = getSpeedSpaceY() + self.accelY*delta
        
        self.x = self.speedX*delta*factor + self.x
        self.y = self.speedY*delta*factor + self.y 

        if getSpeedSpaceX() == getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_right.gif")
        elif getSpeedSpaceX() == -getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_left.gif")
        elif getSpeedSpaceY() == getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_down.gif")
        elif getSpeedSpaceY() == -getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_up.gif")

    def attract(self, xObj, yObj, massObj, theta):
        return [0,0]