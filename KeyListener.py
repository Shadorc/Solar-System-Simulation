from File import *

#Initialisation
speedScrollX=0
speedScrollY=0
speedSpaceX=0
speedSpaceY=0
defSpeed=15
clicked=False
mousePos=[]
megazoom=1

"""'Clics' de souris"""
def mouseClicked(event):
    global clicked, mousePos
    clicked=True
    mousePos=[event.x, event.y]
    
def keyReleased(event) :
    global speedSpaceX, speedSpaceY, speedScrollX, speedScrollY
    
    key = event.keysym
    
    if key == "z":
        speedSpaceY = 0
    if key == "s":
        speedSpaceY = 0
    if key == "q":
        speedSpaceX = 0
    if key == "d":
        speedSpaceX = 0

    if key == "Up":
        speedScrollY = 0
    if key == "Down":
        speedScrollY = 0
    if key == "Right":
        speedScrollX = 0
    if key == "Left":
        speedScrollX = 0
    
def keyPressed(event) :
    global megazoom, speedSpaceX, speedSpaceY, speedScrollX, speedScrollY, defSpeed
    
    key = event.keysym

    if key == "a" :
        megazoom /= 1.1
    elif key == "e" :
        megazoom *= 1.1
        
    if key == "z":
        speedSpaceY=-defSpeed
    if key == "s":
        speedSpaceY = defSpeed
    if key == "q":
        speedSpaceX = -defSpeed
    if key == "d":
        speedSpaceX = defSpeed
        
    if key == "Up":
        speedScrollY = defSpeed
    if key == "Down":
        speedScrollY = -defSpeed
    if key == "Right":
        speedScrollX = -defSpeed
    if key == "Left":
        speedScrollX = defSpeed

def getSpeedScrollX() :
    return speedScrollX
    
def getSpeedScrollY() :
    return speedScrollY
    
def getSpeedSpaceX() :
    return speedSpaceX
    
def getSpeedSpaceY() :
    return speedSpaceY

def getDefSpeed():
    return defSpeed

def getClicked():
    return clicked
    
def setClicked(clicked_):
    global clicked
    clicked = clicked_

def getMousePos():
    return mousePos

def getMegazoom() :
    return megazoom