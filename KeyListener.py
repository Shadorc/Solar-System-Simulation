from File import *

defSpeed=15
maxSpeed=defSpeed*3
speedScrollX=0
speedScrollY=0
speedSpaceX=0
speedSpaceY=0

clicked=False
mousePos=[]
zoom=1

"""'Clics' de souris"""
def mouseClicked(event):
    global clicked, mousePos
    clicked=True
    mousePos=[event.x, event.y]
    
def keyPressed(event) :
    global zoom, speedSpaceX, speedSpaceY, defSpeed
    
    key = event.keysym

    #Zoom
    if key == "a" :
        zoom /= 1.1
    elif key == "e" :
        zoom *= 1.1
    
    #Déplacements du vaisseau
    #FIXME: Si le vaisseau atteint sa vitesse max, il ne pourra jamais ralentir
    if key == "z" and abs(speedSpaceY) < maxSpeed:
        speedSpaceY -= defSpeed
    if key == "s" and abs(speedSpaceY) < maxSpeed:
        speedSpaceY += defSpeed
    if key == "q" and abs(speedSpaceX) < maxSpeed:
        speedSpaceX -= defSpeed
    if key == "d" and abs(speedSpaceX) < maxSpeed:
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

def getZoom() :
    return zoom
