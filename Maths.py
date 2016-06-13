from math import *

G = 6.67e-11

def setG(newG):
    global G
    G = newG

def getG():
    return G


def convMeterToPixel(m):
    """Convertit des mètres en pixels (100 pixels = distance Terre/Soleil en mètres)"""
    return 100*m/1.49e11

def convPixelToMeter(pixels) :
    """Convertit des pixels en mètres"""
    return pixels*1.49e11/100

def getAngle(element, planet):
    """Renvoie l'angle entre element, l'axe des abscisses et planet"""
    angle = atan((element.y-planet.y)/(planet.x-element.x))
    #Si la planète est derrière le vaisseau, on ajoute pi car arctan appartient à -pi/2; pi/2
    if element.x-planet.x > 0:
        angle += pi
    return angle

def getPlanetClicked(objects, mousePos):
    """Renvoie le nom de la planète sur laquelle on a cliqué"""
    for i in range(len(objects)):
        planet = objects[i]
        if(getDistance(mousePos[0], planet.x, mousePos[1], planet.y) <= planet.photo.height()/2):
            return planet.name
    return None

def getDistance(x1, x2, y1, y2) :
    """Renvoie la distance entre deux points"""
    return sqrt((x1-x2)**2+(y1-y2)**2)
    
def PFD(element, objects):
    """Renvoie la projection sur x et y de la somme des forces exercées par les objets sur element"""
    forceX = 0
    forceY = 0
    for i in range(len(objects)):
        obj = objects[i]
        #L'élément ne s'attire pas lui-même, on l'ignore
        if element == obj :
            continue
        theta = getAngle(element, obj)
        #Norme des projections de la force exercée par la planète sur l'élément sous forme de liste
        force = obj.attract(element.x, element.y, element.mass, theta)
        forceX += force[0]
        forceY += force[1]
    return [forceX, forceY]
    
def checkHitbox(element, objects):
    """Renvoie True si element est entré en collision avec un object de la liste objects"""
    for i in range(len(objects)):
        obj = objects[i]
        #On ne veut pas vérifier la collision entre l'objet et lui-même
        if obj == element:
            continue
        if getDistance(obj.x, element.x, obj.y, element.y) < (obj.photo.width()/2 + element.photo.width()/2):
            return True
    return False
