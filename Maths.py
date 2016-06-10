from math import *
from KeyListener import *

G = 6.67e-11

def setG(G_):
    global G
    G=G_

def getG():
    return G

"""Convertit les kms en pixels"""
def convertDist(km):
    #100 pixels = distance Terre/Soleil
    return (100*getZoom()*km)/1.49e8

"""Convertit les pixels en kms"""
def invConvertDist(pixels) :
    return pixels*1.49e8/(100*getZoom())
    
"""Loi des cosinus, c étant le côté opposé à l'angle"""
def getAngle(element, planet):
    angle = atan((element.y-planet.y)/(planet.x-element.x))
    #Si la planète est derrière le vaisseau, on ajoute pi car arctan appartient à -pi/2; pi/2
    if element.x-planet.x > 0:
        angle += pi
    return angle

"""Renvoie le nom de la planète sur lequel on a cliqué"""
def getPlanetClicked(objects, mousePos):
    for i in range(len(objects)):
        planet = objects[i]
        if(getDistance(mousePos[0], planet.x, mousePos[1], planet.y) <= planet.photo.height()/2):
            return planet.name
    return None

"""Renvoie la distance entre deux points"""
def getDistance(x1,x2,y1,y2) :
    return sqrt((x1-x2)**2+(y1-y2)**2)
    
def PFD(element, objects):
    forceX = 0
    forceY = 0
    for i in range(len(objects)):
        obj=objects[i]
        #L'élément ne s'attire pas lui-même, on l'ignore
        if element == obj :
            continue
        theta = getAngle(element, obj)
        #Norme de la force exercée par la planète sur l'élément
        force = obj.attract(element.x, element.y, element.mass, theta)
        forceX += force[0]/element.mass
        forceY += force[1]/element.mass
    return [forceX, forceY]
    
#Renvoie True si obj est entré en collision avec un élément de objects
def checkHitbox(element, objects):
    for i in range(len(objects)):
        obj = objects[i]
        #On ne veut pas vérifier la collision entre l'objet et lui-même
        if obj == element:
            continue
        if getDistance(obj.x, element.x, obj.y, element.y) < obj.photo.width()/2 + element.photo.width()/2:
            return True
    return False