from math import *
from KeyListener import *

"""Convertit les kms en pixels"""
def convertDist(km):
    #100 pixels = distance Terre/Soleil
    return (100*getZoom()*km)/1.49e8

"""Convertit les pixels en kms"""
def invConvertDist(pixels) :
    return pixels*1.49e8/(100*getZoom())
    
"""Loi des cosinus, c étant le côté opposé à l'angle"""
def getAngle(a, b, c):
    return acos((a**2+b**2-c**2)/(2*a*b))

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
    
def PFD(element, objects, soleil):
    forceX = 0
    forceY = 0
    for i in range(len(objects)):
        obj=objects[i]
        #L'élément ne s'attire pas lui-même, on l'ignore
        if element == obj :
            continue
        #ceil: arrondis à la valeur inférieur pour éviter un arcos d'un nombre > 1 dans getAngle()
        a = ceil(getDistance(element.x, soleil.x, element.y, soleil.y)) # distance element<->soleil
        b = ceil(getDistance(element.x, obj.x, element.y, obj.y)) # distance element<->planete
        c = ceil(getDistance(obj.x, soleil.x, obj.y, soleil.y)) # distance planete<->soleil
        theta = getAngle(a,b,c)
        #Norme de la force exercée par la planète sur l'élément
        force = obj.attract(element.x, element.y, element.mass, theta)
        forceX += force[0]/element.mass
        forceY += force[1]/element.mass
    return [forceX, forceY]
