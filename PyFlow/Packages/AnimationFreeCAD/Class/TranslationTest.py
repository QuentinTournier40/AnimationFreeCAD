from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from PyFlow.Packages.AnimationFreeCAD.Class.MouvementEnCours import MouvementEnCours
from PySide2 import QtCore

import functools
import time

class TranslationTest(Mouvement):
    def __init__(self, uneCourbe, unNode):
        Mouvement.__init__(self, unNode)
        self.courbe = uneCourbe
        try:
            self.longueur = self.courbe.Shape.LastParameter
        except:
            self.longueur = self.courbe.Shape.Length
        self.t = 0

    def calculTrajectoire(self, estAllerRetour, duree):
        self.pas = self.longueur / duree
        if(estAllerRetour):
            duree = duree
            self.pas = self.pas * 2
        self.duree = duree
        self.nbrPoints = round(self.longueur / self.pas)
        print(self.nbrPoints)

    def calculDuree(self, uneVitesse):
        duree = self.courbe.Shape.Length / round(uneVitesse)
        return duree

    def mouvement(self, sens, suite):
        distanceParcouru = self.pas * self.t
        try:
            placement = self.courbe.Shape.valueAt(distanceParcouru)
        except:
            placement = self.courbe.Shape.Edges[0].valueAt(distanceParcouru)
        self.objet.Placement.Base = placement

        if(sens):
            self.etape += 1
            stop = self.nbrPoints
        else:
            self.etape -= 1
            stop = -1

        self.t += 0.0319

        if(distanceParcouru >= self.longueur):
            self.timer.stop()
            placement = self.courbe.Shape.valueAt(distanceParcouru)
            self.objet.Placement.Base = placement
            MouvementEnCours.getInstance().enleverNode(self)
            if(suite == ""):
                self.sortieNode.call()
            else:
                exec(suite)

    def execution(self, sens, paramSuite, etape=-1):
        if(etape == -1):
            if(sens):
                self.etape = 0
            else:
                self.etape = self.nbrPoints - 1
        else:
            self.etape = etape
        # Bug de timer lorsque le mouvement est un aller boucle, il se mets à avancer de plus en vite
        # Test : Lorsqu'on fait 2 aller à la suite le 2ème est accéléré, pourquoi ?
        mouvement = functools.partial(self.mouvement, sens=sens, suite=paramSuite)
        MouvementEnCours.getInstance().ajouterNode(self)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)

        self.timer.timeout.connect(mouvement)
        self.timer.start()

    def allerALEtape(self, etape):
        self.etape = int(etape)
        print(self.etape)
        self.objet.Placement.Base = self.pointsTrajectoire[self.etape]
