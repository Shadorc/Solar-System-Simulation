from Planet import *
from Spaceship import *
from Frame import *
import time

frame = Frame()

objects = []

soleil = Planet(None, "Soleil", 1.99e30, 1.39e6, 0)
soleil.x = frame.frame.winfo_screenwidth()/2
soleil.y = frame.frame.winfo_screenheight()/2

mercure = Planet(soleil, "Mercure", 3.29e23, 4.88e3, 5.79e7)
venus = Planet(soleil, "Venus", 4.87e24, 1.21e4, 1.08e8)
terre = Planet(soleil, "Terre", 5.97e24, 1.27e4, 1.49e8)
lune = Planet(terre, "Lune", 7.35e22, 3.47e3, 3.84e5)
mars = Planet(soleil, "Mars", 6.42e23, 6.78e3, 2.27e8)
jupiter = Planet(soleil, "Jupiter", 1.90e27, 1.40e5, 7.79e8) 
saturne = Planet(soleil, "Saturne", 5.68e26, 1.16e5, 1.42e9)
uranus = Planet(soleil, "Uranus", 8.68e25, 5.07e4, 2.88e9)
neptune = Planet(soleil, "Neptune", 1.02e26, 4.92e4, 4.50e9)

vaisseau = Spaceship(soleil.x, soleil.y)

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

FPS=60
sleepTime = 1/FPS
increaseTime = 31536000
elapsed = 0
while True:
    frame.univers.delete('all')
    #Parcourt tous les objets, les actualise et les affiche
    for i in range(len(objects)):
        obj = objects[i]
        obj.move(sleepTime*increaseTime) #1 sec -> 365 jours (31536000s)
        frame.draw(obj)
        frame.setInfos(soleil.x, soleil.y, elapsed)
    
    #A retravailler
    if getClicked():
        try:
            frame.createPopup(getInfoPlanet(getPlanetClicked(objects, getMousePos())))
        except:
            print("Clique en dehors d'une planète")
        setClicked(False)
        
    frame.frame.update()
    time.sleep(sleepTime)
    elapsed += sleepTime*increaseTime
