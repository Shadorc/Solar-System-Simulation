from tkinter import *
from KeyListener import *


class Spaceship():
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        
        self.photo = PhotoImage(file="images/Spaceship_up.gif")
    

    def move(self, delta) :
        
        if getX() == -getSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_right.gif")
        
        if getX() == getSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_left.gif")
            
        if getY() == -getSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_down.gif")
            
        if getY() == getSpeed() :
            self.photo = PhotoImage(file="images/Spaceship_up.gif")
