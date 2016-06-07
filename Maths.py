from math import *

def convertDist(km):
        #100 pixels = distance Terre/Soleil
        return 100*km/1.49e8

def invConvertDist(pixels):
         return pixels/100*1.49e8

def getPlanetClicked(objects, mousePos):
    for i in range(len(objects)):
        planet = objects[i]
        print(sqrt((mousePos[0]-planet.x)**2 + (mousePos[1]-planet.y)**2), planet.photo.height()/2)
        if(sqrt((mousePos[0]-planet.x)**2 + (mousePos[1]-planet.y)**2) <= planet.photo.height()/2):
            return planet.name
