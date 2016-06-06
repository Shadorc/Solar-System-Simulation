def convertDist(km):
        #100 pixels = distance Terre/Soleil
        return 100*km/1.49e8

def invConvertDist(pixels):
         return pixels/100*1.49e8
