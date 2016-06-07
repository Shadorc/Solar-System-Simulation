X=0
Y=0

def keyPressed(event) :
    
    global X,Y
    
    touche = event.keysym
    speed=10
    
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
