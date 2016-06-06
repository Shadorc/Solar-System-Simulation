from Planet import *
from Frame import *
import time

frame = Frame()

objects = []

soleil = Planet(None, "soleil.gif", 2e30, 1.4e6, 0)
terre = Planet(soleil, "terre.gif", 6e24, 12540, 1.49e8)
lune = Planet(terre, "lune.gif", 7.4e22, 3474, 3.8e7)
mars = Planet(soleil, "mars.gif", 6.39e23, 6779, 2.27e8)
venus = Planet(soleil, "lune.gif", 4.867e24, 12104, 1.08e8)

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
        obj.move(1/FPS)
        frame.draw(obj)
    frame.frame.update()
    time.sleep(1/FPS)
