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

mercure = Planet(soleil, "Mercure", 3.29e23, 4.88e3, 5.79e7, 47879.56, 308)
venus = Planet(soleil, "Venus", 4.87e24, 1.21e4, 1.08e8, 35057.23, 168)
terre = Planet(soleil, "Terre", 5.97e24, 1.27e4, 1.49e8, 29846.70, 175)
lune = Planet(terre, "Lune", 7.35e22, 3.47e3, 3.84e5, 1018.32, 113.8)
mars = Planet(soleil, "Mars", 6.42e23, 6.78e3, 2.27e8, 24181.13, 313)
jupiter = Planet(soleil, "Jupiter", 1.90e27, 1.40e5, 7.79e8, 13053.31, 309) 
saturne = Planet(soleil, "Saturne", 5.68e26, 1.16e5, 1.42e9, 30573.51, 168)
uranus = Planet(soleil, "Uranus", 8.68e25, 5.07e4, 2.88e9, 6788.80, 353)
neptune = Planet(soleil, "Neptune", 1.02e26, 4.92e4, 4.50e9, 5431.04, 324)

vaisseau = Spaceship(300, 300)

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
elapsed = 0 #Temps écoulé
startloop = time.time()  

def upPos():
    if vaisseau.x < vaisseau.photo.width()/2:
        setSpeedScrollX(-vaisseau.speedX)
    elif vaisseau.x > frame.frameW - vaisseau.photo.width():
        setSpeedScrollX(-vaisseau.speedX)
    else:
        setSpeedScrollX(0)

    if vaisseau.y < vaisseau.photo.height()/2:
        setSpeedScrollY(-vaisseau.speedY)
    elif vaisseau.y > frame.frameH + vaisseau.photo.height():
        setSpeedScrollY(-vaisseau.speedY)
    else:
        setSpeedScrollY(0)
             
while True:
    #Le temps qu'il s'est écoulé depuis le dernier tour de boucle
    delta = time.time()-startloop
    startloop = time.time()

    multipleTime=frame.time.get()*2.628e6 #Convertit les mois en secondes
    
    frame.univers.delete('all')
    
    #Parcourt tous les objets, les actualise et les affiche
    for i in range(len(objects)):
        obj = objects[i]
        
        #On convertit en km le TRC qui est en mètre
        TRC = PFD(obj, objects)
        obj.accelX = TRC[0]
        obj.accelY = TRC[1]
        
        # if checkHitbox(obj, objects):
        #     obj.photo = PhotoImage(file='images/explosion.gif')
        # else:
        obj.move(delta*multipleTime)
        points.append(Point(obj.x, obj.y))
        frame.draw(obj)
        frame.setInfos(round(vaisseau.x), round(vaisseau.y), elapsed)
        
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
