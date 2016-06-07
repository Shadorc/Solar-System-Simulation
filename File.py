def getInfoPlanet(planetName):
    file = open('BDD_planetes.txt', 'r')
    lines = file.readlines()
    file.close()
    for i in range(len(lines)):
        line = lines[i]
        mots = line.split(', ')
        if mots[0] == planetName:
            return mots
            
