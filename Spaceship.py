from tkinter import *
from KeyListener import *

class Spaceship():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.photo = PhotoImage(file="images/Spaceship_up.gif")

    def move(self, delta) :
        """Permet de gérer l'affichage du vaisseau selon sons sens de déplacement"""
        factor = 10**-5
        self.x = getSpeedSpaceX()*delta*factor + self.x + getSpeedScrollX()
        self.y = getSpeedSpaceY()*delta*factor + self.y + getSpeedScrollY()

        if getSpeedSpaceX() == getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_right.gif")
        elif getSpeedSpaceX() == -getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_left.gif")
        elif getSpeedSpaceY() == getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_down.gif")
        elif getSpeedSpaceY() == -getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_up.gif")
