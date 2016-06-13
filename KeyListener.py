from Maths import *

defaultSpeed = convMeterToPixel(21000*1e10)
maxSpeed = defaultSpeed*3

speedScrollX = 0
speedScrollY = 0
speedSpaceX = 0
speedSpaceY = 0

clicked = False
mousePos = []

def mouseClicked(event):
    global clicked, mousePos
    clicked=True
    mousePos=[event.x, event.y]
    
def keyPressed(event) :
    global speedSpaceX, speedSpaceY, defaultSpeed
    
    key = event.keysym
    
    #Déplacements du vaisseau
    #Haut
    if key == "z" and speedSpaceY > -maxSpeed:
        speedSpaceY -= defaultSpeed
    #Bas
    if key == "s" and speedSpaceY < maxSpeed:
        speedSpaceY += defaultSpeed
    #Gauche
    if key == "q" and speedSpaceX > -maxSpeed:
        speedSpaceX -= defaultSpeed
    #Droite
    if key == "d" and speedSpaceX < maxSpeed:
        speedSpaceX += defaultSpeed

def getSpeedScrollX() :
    return speedScrollX
    
def getSpeedScrollY() :
    return speedScrollY

def setSpeedScrollX(newSpeedScrollX):
    global speedScrollX
    speedScrollX = newSpeedScrollX

def setSpeedScrollY(newSpeedScrollY):
    global speedScrollY
    speedScrollY = newSpeedScrollY
    
def getSpeedSpaceX() :
    return speedSpaceX
    
def getSpeedSpaceY() :
    return speedSpaceY

def getClicked():
    return clicked
    
def setClicked(clicked_):
    global clicked
    clicked = clicked_

def getMousePos():
    return mousePos
