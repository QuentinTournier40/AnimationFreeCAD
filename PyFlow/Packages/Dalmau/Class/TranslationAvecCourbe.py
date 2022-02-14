import FreeCAD
from PyFlow.Packages.Dalmau.Class.Mouvement import NOMBRE_D_OR, Mouvement
from PySide import QtCore
import functools
import time

class TranslationAvecCourbe(Mouvement):
    
    def __init__(self, unNode):
        super().__init__(unNode)
        self.courbe = unNode.courbe
        
        if(not(self.estAllerRetour)):
            self.nbrPoints = round(NOMBRE_D_OR * self.duree)
        else:
            self.nbrPoints = round(NOMBRE_D_OR * self.duree / 2)
        self.pointsTrajectoire = self.creerListeDePointsAvecUneCourbe(self.courbe)

    def creerListeDePointsAvecUneCourbe(self, uneCourbe):
        return uneCourbe.Shape.discretize(self.nbrPoints)

    def mouvement(self, sens,suite):
        self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])

        if(sens == True):
            self.etape += 1
            stop = self.nbrPoints
        else:
            self.etape -= 1
            stop = -1

        if(self.etape == stop):
            self.timer.stop()
            print(time.time() - self.monTemps)
            exec(suite)


    def mouvementSansBoucle(self, sens, paramSuite):
        if(sens == True):
            self.etape = 0
            mouvement = functools.partial(self.mouvement, sens = True, suite = paramSuite)
            print("Aller")
        else:
            self.etape = self.nbrPoints - 1
            print("Retour")
            mouvement = functools.partial(self.mouvement, sens = False, suite = paramSuite)

        self.timer.timeout.connect(mouvement)
        self.timer.start(20)

    
    def mouvementBoucle(self):
        self.mouvementSansBoucle(True,"self.mouvementBoucle()")

    def mouvementAller(self):
        self.mouvementSansBoucle(True,"self.sortieNode.call()")
    
    def mouvementAllerRetourSansBoucle(self, sortie):
        self.mouvementSansBoucle(True,"self.mouvementSansBoucle(False, \""+ sortie + "\")")

    def mouvementAllerRetourBoucle(self):
        self.mouvementAllerRetourSansBoucle("self.mouvementAllerRetourBoucle()")
    #def mouvementAllerRetourBoucle(self):




    def translater(self):
        if(self.estBoucle and self.estAllerRetour):
            self.mouvementAllerRetourBoucle()
        elif(self.estBoucle and not(self.estAllerRetour)):
            self.mouvementBoucle()
        elif(self.estAllerRetour and not(self.estBoucle)):
            self.mouvementAllerRetourSansBoucle("self.sortieNode.call()")
        else:
            self.mouvementAller()
        self.monTemps = time.time()