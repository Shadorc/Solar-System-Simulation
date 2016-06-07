from Planet import *
from Frame import *
import time

frame = Frame()

objects = []

soleil = Planet(None, "soleil.gif", 1.99e30, 1.39e6, 0)
soleil.x = frame.frame.winfo_screenwidth()/2
soleil.y = frame.frame.winfo_screenheight()/2
mercure = Planet(soleil, "mercure.gif", 3.29e23, 4.88e3, 5.79e7)
venus = Planet(soleil, "venus.gif", 4.87e24, 1.21e4, 1.08e8)
terre = Planet(soleil, "terre.gif", 5.97e24, 1.27e4, 1.49e8)
lune = Planet(terre, "lune.gif", 7.35e22, 3.47e3, 3.84e5)
mars = Planet(soleil, "mars.gif", 6.42e23, 6.78e3, 2.27e8)
jupiter = Planet(soleil, "jupiter.gif", 1.90e27, 1.40e5, 7.79e8) 
saturne = Planet(soleil, "saturne.gif", 5.68e26, 1.16e5, 1.42e9)
uranus = Planet(soleil, "uranus.gif", 8.68e25, 5.07e4, 2.88e9)
neptune = Planet(soleil, "neptune.gif", 1.02e26, 4.92e4, 4.50e9)


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

FPS=30
while True:
    frame.univers.delete('all')
    for i in range(len(objects)):
        obj = objects[i]
        obj.move(1/FPS*31536000)
        frame.draw(obj)
    frame.frame.update()
    time.sleep(1/FPS)
