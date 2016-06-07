from Planet import *
from Spaceship import *
from Frame import *
import time

frame = Frame()

objects = []

soleil = Planet(None, "Soleil", "soleil.gif", 1.99e30, 1.39e6, 0)
soleil.x = frame.frame.winfo_screenwidth()/2
soleil.y = frame.frame.winfo_screenheight()/2

mercure = Planet(soleil, "Mercure", "mercure.gif", 3.29e23, 4.88e3, 5.79e7)
venus = Planet(soleil, "Venus", "venus.gif", 4.87e24, 1.21e4, 1.08e8)
terre = Planet(soleil, "Terre", "terre.gif", 5.97e24, 1.27e4, 1.49e8)
lune = Planet(terre, "Lune", "lune.gif", 7.35e22, 3.47e3, 3.84e5)
mars = Planet(soleil, "Mars", "mars.gif", 6.42e23, 6.78e3, 2.27e8)
jupiter = Planet(soleil, "Jupiter", "jupiter.gif", 1.90e27, 1.40e5, 7.79e8) 
saturne = Planet(soleil, "Saturne", "saturne.gif", 5.68e26, 1.16e5, 1.42e9)
uranus = Planet(soleil, "Uranus", "uranus.gif", 8.68e25, 5.07e4, 2.88e9)
neptune = Planet(soleil, "Neptune", "neptune.gif", 1.02e26, 4.92e4, 4.50e9)

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

FPS=30
elapsed = 0
while True:
    frame.univers.delete('all')
    for i in range(len(objects)):
        obj = objects[i]
        obj.move(1/FPS*10000000) #1 sec -> 365 jours (31536000s)
        frame.draw(obj)
        elapsed += 1/FPS*10000000
        frame.setInfos(soleil.x, soleil.y, elapsed)
    if getClicked():
        frame.createPopup(getInfoPlanet(getPlanetClicked(objects, getMousePos())))
        setClicked(False)
    frame.frame.update()
    time.sleep(1/FPS)
