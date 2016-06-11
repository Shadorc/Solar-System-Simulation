from File import *
from Maths import *

defSpeed = convMeterToPixel(21000*1e10)
maxSpeed = defSpeed*3

speedScrollX = 0
speedScrollY = 0
speedSpaceX = 0
speedSpaceY = 0

clicked = False
mousePos = []

"""'Clics' de souris"""
def mouseClicked(event):
    global clicked, mousePos
    clicked=True
    mousePos=[event.x, event.y]
    
def keyPressed(event) :
    global speedSpaceX, speedSpaceY, defSpeed
    
    key = event.keysym
    
    #Déplacements du vaisseau
    #Haut
    if key == "z" and speedSpaceY > -maxSpeed:
        speedSpaceY -= defSpeed
    #Bas
    if key == "s" and speedSpaceY < maxSpeed:
        speedSpaceY += defSpeed
    #Gauche
    if key == "q" and speedSpaceX > -maxSpeed:
        speedSpaceX -= defSpeed
    #Droite
    if key == "d" and speedSpaceX < maxSpeed:
        speedSpaceX += defSpeed

def getSpeedScrollX() :
    return speedScrollX
    
def getSpeedScrollY() :
    return speedScrollY

def setSpeedScrollX(speedScrollX_):
    global speedScrollX
    speedScrollX = speedScrollX_

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
