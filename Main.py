from Planet import *
from Spaceship import *
from Frame import *
from Maths import *
from Point import *
import time

frame = Frame()

objects = []
points = []

soleil = Planet(None, "Soleil", 1.99e30, 1.39e6, 0, 0, 0)
soleil.x = frame.frame.winfo_screenwidth()/2
soleil.y = frame.frame.winfo_screenheight()/2
soleil.speedX = 0
soleil.speedY = 0

#parent, name, mass, diam, dist, speed, theta
mercure = Planet(soleil, "Mercure", 3.29e23, 4.88e3, 5.79e10, 47879.56, 308)
venus = Planet(soleil, "Venus", 4.87e24, 1.21e4, 1.08e11, 35057.23, 168)
terre = Planet(soleil, "Terre", 5.97e24, 1.27e4, 1.49e11, 29846.70, 175)
lune = Planet(terre, "Lune", 7.35e22, 3.47e3, 3.84e8, 1018.32, 113.8)
mars = Planet(soleil, "Mars", 6.42e23, 6.78e3, 2.27e11, 24181.13, 313)
jupiter = Planet(soleil, "Jupiter", 1.90e27, 1.40e5, 7.79e11, 13053.31, 309) 
saturne = Planet(soleil, "Saturne", 5.68e26, 1.16e5, 1.42e12, 30573.51, 168)
uranus = Planet(soleil, "Uranus", 8.68e25, 5.07e4, 2.88e12, 6788.80, 353)
neptune = Planet(soleil, "Neptune", 1.02e26, 4.92e4, 4.50e12, 5431.04, 324)

vaisseau = Spaceship(100, 100)

objects.append(soleil)
objects.append(mercure)
objects.append(venus)
objects.append(terre)
objects.append(lune)
objects.append(mars)
objects.append(jupiter)
objects.append(saturne)
objects.append(uranus)
objects.append(neptune)
objects.append(vaisseau)

##Boucle principale
FPS=1000
sleepTime = 1/FPS
elapsed = 0
startloop = time.time()  

def upPos():
    offset = 100
    #Bord gauche
    if vaisseau.x < vaisseau.photo.width()/2 + offset:
        setSpeedScrollX(-getSpeedSpaceX())
    #Bord droit
    elif vaisseau.x > frame.univers.winfo_width() - vaisseau.photo.width() - offset:
        setSpeedScrollX(-getSpeedSpaceX())
    else:
        setSpeedScrollX(0)

    #Bord haut
    if vaisseau.y < vaisseau.photo.height()/2 + offset:
        setSpeedScrollY(-getSpeedSpaceY())
    #Bord bas
    elif vaisseau.y > frame.univers.winfo_height() - vaisseau.photo.height() - offset:
        setSpeedScrollY(-getSpeedSpaceY())
    else:
        setSpeedScrollY(0)
             
while True:
    #Le temps qu'il s'est écoulé depuis le dernier tour de boucle
    delta = time.time()-startloop
    startloop = time.time()

    multipleTime = frame.time.get()*2.628e6 #Convertit les mois en secondes
    
    frame.univers.delete('all')
    
    #Parcourt tous les objets, les actualise et les affiche
    for i in range(len(objects)):
        obj = objects[i]
        
        #On calcule toutes les forces appliquées sur un objet et on modifie son accélération en conséquence
        TRC = PFD(obj, objects)
        obj.accelX = TRC[0]
        obj.accelY = TRC[1]
        
        # if checkHitbox(obj, objects):
        #     obj.photo = PhotoImage(file='images/explosion.gif')
        # else:
        obj.move(delta*multipleTime)
        points.append(Point(obj.x, obj.y))
        frame.draw(obj)
        frame.setInfos(round(soleil.x-vaisseau.x), round(soleil.y-vaisseau.y), elapsed)
        
    #Trajectoire des objets
    i=0
    while i < len(points):
        pt = points[i]
        #On a activé l'affichage des trajectoires
        if frame.showTrace.get() == 1:
            frame.drawPoint(pt)
        pt.count += 1
        if pt.count >= 50:
            points.remove(pt)
        i+=1
    
    upPos()
    
    #Si l'utilisateur a cliqué affiche les infos de la planète
    if getClicked():
        infoPlanet = getInfoPlanet(getPlanetClicked(objects, getMousePos()))
        #S'il n'a pas cliqué en dehors d'une planète        
        if infoPlanet != None:
            frame.createPopup(infoPlanet)
        setClicked(False)
    
    frame.frame.update()
    time.sleep(sleepTime)
    elapsed += delta*multipleTime
