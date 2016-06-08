#Importation des différents modules
from File import *


#Initialisation
speedX=0
speedY=0
defSpeed=15
clicked=False
mousePos=[]
megazoom = 1


## Fonctions gérant les évènements

def mouseClicked(event):
    """'Clics' de souris"""
    
    global clicked, mousePos
    clicked=True
    mousePos=[event.x, event.y]


#Touche pressée
def scrollPressed(event) :
    """Touches directionnelles"""
    
    global speedX, speedY, defSpeed

    key = event.keysym

    if key == "Up":
        speedY = defSpeed
    elif key == "Down":
        speedY = -defSpeed
    elif key == "Right":
        speedX = -defSpeed
    elif key == "Left":
        speedX = defSpeed


def zoomPressed(event):
    """Zoom (+) ou dézoom (-)"""
    
    global megazoom
    key = event.keysym
    
    if key == "z" :
        megazoom = 1.1
    elif key == "s" :
        megazoom = 1/1.1
        
        
#Touche relachée    
def scrollReleased(event) :
    """Touches directionnelles"""
    
    global speedX, speedY
    
    key = event.keysym

    if key == "Up":
        speedY = 0
    elif key == "Down":
        speedY = 0
    elif key == "Right":
        speedX = 0
    elif key == "Left":
        speedX = 0


def zoomReleased(event):
    """Zoom ou dézoom"""
    
    global megazoom
    key = event.keysym
    
    if key == "z" or key == "s":
        megazoom = 1


#Fonctions globales
def keyPressed(event):
    scrollPressed(event)
    zoomPressed(event)

def keyReleased(event):
    scrollReleased(event)
    zoomReleased(event)



## Fonctions "récupératrices"

def getSpeedX() :
    return speedX
    
def getSpeedY() :
    return speedY

def getDefSpeed():
    return defSpeed

def getClicked():
    return clicked
    
def setClicked(clicked_):
    global clicked
    clicked = clicked_

def getMousePos():
    return mousePos

def getMegazoom():
    return megazoom