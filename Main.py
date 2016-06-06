from Planet import *
from Frame import *
import time

frame = Frame()

objects = []

soleil = Planet(None, "soleil.gif", 1.99e30, 1.39e6, 0)
terre = Planet(soleil, "terre.gif", 5.97e24, 1.27e4, 1.49e8)
lune = Planet(terre, "lune.gif", 7.35e22, 3.47e3, 3.84e5)
mars = Planet(soleil, "mars.gif", 6.42e23, 6.78e3, 2.27e8)
venus = Planet(soleil, "venus.gif", 4.87e24, 1.21e4, 1.08e8)

objects.append(soleil)
objects.append(terre)
objects.append(lune)
objects.append(mars)
objects.append(venus)

FPS=30
while True:
    frame.univers.delete('all')
    for i in range(len(objects)):
        obj = objects[i]
        obj.move(1/FPS*100)
        frame.draw(obj)
    frame.frame.update()
    time.sleep(1/FPS)
