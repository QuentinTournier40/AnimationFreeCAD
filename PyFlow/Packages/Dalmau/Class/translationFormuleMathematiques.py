from PyFlow.Packages.Dalmau.Class.TranslationAvecCourbe import TranslationAvecCourbe
from PySide import QtCore
import functools
import FreeCAD
import time

class translationFormuleMathematiques(TranslationAvecCourbe):
    def __init__(self, equationX, equationY, equationZ, duree, objet):
        self.equationX = equationX
        self.equationY = equationY
        self.equationZ = equationZ
        self.t = 0
        self.duree = duree
        self.objet = objet
        self.stop = self.duree
        print("Stop : "  + str(self.stop))

    def calculerPoint(self):
        t = self.t
        print(t)
        posX = eval(self.equationX)
        posY = eval(self.equationY)
        posZ = eval(self.equationZ)
        return FreeCAD.Vector(posX,posY,posZ)
    
    def execution2(self):
        print("execution")
        placementObjet = self.calculerPoint()
        self.objet.Placement.Base = placementObjet
        self.t += 0.0319
        print("t : "  + str(self.t))

        if(self.t >= self.stop):
            self.timer.stop()
            print(time.time() - self.temps)

    def lancerTimer(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)
        mouvement = functools.partial(self.execution2)
        self.timer.timeout.connect(mouvement)
        self.timer.start()
        self.temps = time.time()