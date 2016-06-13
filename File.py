def getInfoPlanet(planetName):
    """Renvoie les informations sur une planète contenues dans la base de données"""
    file = open('BDD_planetes.txt', 'r')
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        line = lines[i]
        infos = line.split(', ')
        if infos[0] == planetName:
            return infos
    return None
