#Fonction
def getInfoPlanet(planetName):
    """Fonction récupérant les informations intéressantes sur une planète"""
    
    file = open('BDD_planetes.txt', 'r')
    lines = file.readlines()
    file.close()
    
    for i in range(len(lines)):
        line = lines[i]
        mots = line.split(', ')
        if mots[0] == planetName:
            return mots
            
            
def getMenu():
    """Fonction récupérant le menu"""
    
    file = open('Menu.txt', 'r')
    lines = file.readlines()
    file.close()
    
    for i in range(len(lines)):
        line = lines[i]
        mots = line.split(', ')
        if mots[0] == planetName:
            return mots        infos = line.split(', ')
        if infos[0] == planetName:
            return infos
    return None