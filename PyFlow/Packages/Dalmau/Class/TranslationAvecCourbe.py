from PyFlow.Packages.Dalmau.Class.Mouvement import *
from PyFlow.Packages.Dalmau.Class.NodeCourant import NodeCourant
from PySide2 import QtCore

import functools
import time

class TranslationAvecCourbe(Mouvement):
    def __init__(self, uneCourbe, unNode):
        Mouvement.__init__(self,unNode)
        self.courbe = uneCourbe
        self.mouvementAEteBoucle = False

    def calculTrajectoire(self, estAllerRetour, duree):
        if(estAllerRetour):
            duree = duree / 2
        self.nbrPoints = round(NOMBRE_D_OR * duree)
        self.pointsTrajectoire = self.courbe.Shape.discretize(self.nbrPoints)

    def calculDuree(self, uneVitesse):
        duree = self.courbe.Shape.Length / round(uneVitesse)
        return duree

    def setObjet(self, objet):
        self.objet = objet

    def mouvement(self, sens, suite):
        self.objet.Placement.Base = self.pointsTrajectoire[self.etape]
        
        if(sens):
            self.etape += 1
            stop = self.nbrPoints
        else:
            self.etape -= 1
            stop = -1

        if(self.etape == stop):
            print(time.time() - self.monTemps)
            self.timer.stop()
            NodeCourant.getInstance().enleverNode(self)
            exec(suite)           

    def execution(self, sens, paramSuite):
        if(sens):
            self.etape = 0
            mouvement = functools.partial(self.mouvement, sens = True, suite = paramSuite)
            print("Aller")
        else:
            self.etape = self.nbrPoints - 1
            print("Retour")
            mouvement = functools.partial(self.mouvement, sens = False, suite = paramSuite)

        #Bug de timer lorsque le mouvement est un aller boucle, il se mets à avancer de plus en vite
        #Test : Lorsqu'on fait 2 aller à la suite le 2ème est accéléré, pourquoi ?
        NodeCourant.getInstance().ajouterNode(self)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)
        
        self.timer.timeout.connect(mouvement)
        self.timer.start()

    def executionAller(self, sortie):
        self.execution(True,sortie)
        self.monTemps = time.time()
    
    def executionAllerRetour(self, sortie):
        self.execution(True,"self.execution(False, \""+ sortie + "\")")
        self.monTemps = time.time()

    def executionAllerBoucle(self):
        self.execution(True, "self.executionAllerBoucle()")
        self.monTemps = time.time()

    def executionBoucleAllerRetour(self):
        self.executionAllerRetour("self.executionBoucleAllerRetour()")
        self.monTemps = time.time()
    
    def allerALEtape(self, etape):
        self.etape = int(etape)
        print(self.etape)
        self.objet.Placement.Base = self.pointsTrajectoire[self.etape]