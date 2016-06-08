"""Fonction récupérant les informations intéressantes sur une planète"""
def getInfoPlanet(planetName):
    file = open('BDD_planetes.txt', 'r')
    lines = file.readlines()
    file.close()
    
    for i in range(len(lines)):
        line = lines[i]
        infos = line.split(', ')
        if infos[0] == planetName:
            return infos
    return None
