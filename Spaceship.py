from tkinter import *
from KeyListener import *

class Spaceship():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.photo = PhotoImage(file="images/Spaceship_up.gif")

    def move(self, delta) :
        """Permet de gérer l'affichage du vaisseau selon sons sens de déplacement"""
        if getSpeedX() == -getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_right.gif")
        elif getSpeedX() == getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_left.gif")
        elif getSpeedY() == -getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_down.gif")
        elif getSpeedY() == getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_up.gif")
