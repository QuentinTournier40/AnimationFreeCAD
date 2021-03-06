from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from PyFlow.Packages.AnimationFreeCAD.Class.MouvementEnCours import MouvementEnCours
from PySide2 import QtCore

import functools

class TranslationAvecCourbe(Mouvement):
    def __init__(self, uneCourbe, unNode):
        Mouvement.__init__(self, unNode)
        self.courbe = uneCourbe

    def calculTrajectoire(self, estAllerRetour, duree):
        if(estAllerRetour):
            duree = duree / 2
        self.nbrPoints = round(NOMBRE_D_OR * duree)
        self.pointsTrajectoire = self.courbe.Shape.discretize(self.nbrPoints)

    def calculDuree(self, uneVitesse):
        duree = self.courbe.Shape.Length / round(uneVitesse)
        return duree

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

    def mouvement(self, sens, suite):
        self.objet.Placement.Base = self.pointsTrajectoire[self.etape]
        if(sens):
            self.etape += 1
            stop = self.nbrPoints
        else:
            self.etape -= 1
            stop = -1

        if(self.etape == stop):
            self.timer.stop()
            MouvementEnCours.getInstance().enleverNode(self)
            if(suite == ""):
                self.sortieNode.call()
            else:
                exec(suite)

    def allerALEtape(self, etape):
        self.etape = int(etape)
        self.objet.Placement.Base = self.pointsTrajectoire[self.etape]
