from math import *
from KeyListener import *

"""Convertit les kms en pixels"""
def convertDist(km):
    #100 pixels = distance Terre/Soleil
    return (100*getMegazoom()*km)/1.49e8

def invconvertDist(pixels) :
    return pixels*1.49e8/(100*getMegazoom())
    
#Loi des cosinus, c étant le côté opposé à l'angle
def getAngle(a, b, c):
    return acos((a**2+b**2-c**2)/(2*a*b))


def getPlanetClicked(objects, mousePos):
    """Quand on clique sur une planète, récupère ses informations"""
    for i in range(len(objects)):
        planet = objects[i]
        if(sqrt((mousePos[0]-planet.x)**2 + (mousePos[1]-planet.y)**2) <= planet.photo.height()/2):
            return planet.name
    return None

def getDistance(x1,x2,y1,y2) :
    return sqrt((x1-x2)**2+(y1-y2)**2)
    
def PFD(element, objects, soleil):
    forceX = 0
    forceY = 0
    for i in range(len(objects)):
        obj=objects[i]
        #L'élément ne s'attire pas lui-même
        if element == obj :
            continue
        a = ceil(getDistance(element.x, soleil.x, element.y, soleil.y)) # distance element soleil
        b = ceil(getDistance(element.x, obj.x, element.y, obj.y)) # distance element planete
        c = ceil(getDistance(obj.x, soleil.x, obj.y, soleil.y)) # distance planete soleil
        print(obj.name,a,b,c)
        theta = getAngle(a,b,c)
        force = obj.attract(element.x, element.y, element.mass, theta)
        forceX += force[0]/element.mass
        forceY += force[1]/element.mass
    return [forceX, forceY]