from tkinter import *
from KeyListener import *

class Spaceship():
    
    def __init__(self, x, y):
        self.speedX = 0
        self.speedY = 0
        self.accel = 0
        self.x = x
        self.y = y
        self.photo = PhotoImage(file="images/Spaceship_up.gif")

    def move(self, delta) :
        """Permet de gérer l'affichage du vaisseau selon sons sens de déplacement"""
        self.speedX = getSpeedSpaceX()
        self.speedY = getSpeedSpaceY()
        
        factor = 10**-5
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
