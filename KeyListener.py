from File import *

X=0
Y=0
speed=15
clicked = False
mousePos=[]

def mouseClicked(event):
    global clicked, mousePos
    clicked=True
    mousePos=[event.x, event.y]

def keyPressed(event) :
    
    global X,Y,speed
    
    touche = event.keysym
    
    if touche == "Up":
        Y = speed
    elif touche == "Down":
        Y = -speed
    elif touche == "Right":
        X = -speed
    elif touche == "Left":
        X = speed
        
def keyReleased(event) :
    
    global X,Y
    
    touche = event.keysym

    if touche == "Up":
        Y = 0
    elif touche == "Down":
        Y = 0
    elif touche == "Right":
        X = 0
    elif touche == "Left":
        X = 0
        
def getX() :
    return X
    
def getY() :
    return Y

def getSpeed():
    return speed

def getClicked():
    return clicked
    
def setClicked(click):
    global clicked
    clicked = click

def getMousePos():
    return mousePos
