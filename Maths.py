#Importation des différents modules
from math import *
from KeyListener import *

#Fonctions
def convertDist(km):
    """Convertit les kms en pixels"""
    
    #100 pixels = distance Terre/Soleil
    return 100*km/1.49e8


def invConvertDist(pixels):
    """Réciproque de la fonction précédente"""
    
    return pixels/100*1.49e8


def getPlanetClicked(objects, mousePos):
    """Quand on clique sur une planète, récupère ses informations"""
    
    for i in range(len(objects)):
        planet = objects[i]
        if(sqrt((mousePos[0]-planet.x)**2 + (mousePos[1]-planet.y)**2) <= planet.photo.height()/2):
            return planet.name