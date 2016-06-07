from tkinter import *
from KeyListener import *

class Spaceship():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.photo = PhotoImage(file="images/Spaceship_up.gif")
    

    def move(self, delta) :
        if getSpeedX() == -getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_right.gif")
        if getSpeedX() == getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_left.gif")
        if getSpeedY() == -getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_down.gif")
        if getSpeedY() == getDefSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_up.gif")
