from File import *

speedX=0
speedY=0
defSpeed=15
clicked=False
mousePos=[]

def mouseClicked(event):
    global clicked, mousePos
    clicked=True
    mousePos=[event.x, event.y]

#Touche pressée
def keyPressed(event) :
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

#Touche relachée    
def keyReleased(event) :
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
