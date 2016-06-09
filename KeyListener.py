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
    global speedSpaceX, speedSpaceY
    
    key = event.keysym
    
    # if key == "z":
    #     speedSpaceY = 0
    # if key == "s":
    #     speedSpaceY = 0
    # if key == "q":
    #     speedSpaceX = 0
    # if key == "d":
    #     speedSpaceX = 0

    
def keyPressed(event) :
    global megazoom, speedSpaceX, speedSpaceY, defSpeed
    
    key = event.keysym

    if key == "a" :
        megazoom /= 1.1
    elif key == "e" :
        megazoom *= 1.1
    
    #Déplacements du vaisseau
    if key == "z" and speedSpaceY < defSpeed*3:
        speedSpaceY -= defSpeed
    if key == "s" and speedSpaceY < defSpeed*3:
        speedSpaceY += defSpeed
    if key == "q" and speedSpaceX < defSpeed*3:
        speedSpaceX -= defSpeed
    if key == "d" and speedSpaceX < defSpeed*3:
        speedSpaceX += defSpeed


def getSpeedScrollX() :
    return speedScrollX

def setSpeedScrollX(speedScrollX_):
    global speedScrollX
    speedScrollX = speedScrollX_
    
def getSpeedScrollY() :
    return speedScrollY

def setSpeedScrollY(speedScrollY_):
    global speedScrollY
    speedScrollY = speedScrollY_
    
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