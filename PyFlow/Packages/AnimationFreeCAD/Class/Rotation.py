from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from PyFlow.Packages.AnimationFreeCAD.Class.NodeCourant import NodeCourant
from PySide import QtCore

import functools
import time
import math

class Rotation(Mouvement):

    def __init__(self, axeDeRotation, centreDeRotation, angleDeDebut, angleDeFin, unNode):
        super().__init__(unNode)
        self.axeDeRotation = axeDeRotation
        self.centreDeRotation = centreDeRotation
        self.angleDeDebut = angleDeDebut
        self.angleDeFin = angleDeFin
        self.mouvementAEteBoucle = False

    def calculTrajectoire(self, estAllerRetour, duree):
        if(estAllerRetour):
            duree = duree / 2
        self.nbrPoints = round(NOMBRE_D_OR * duree)
        self.angleARepeter = (self.angleDeFin - self.angleDeDebut) / self.nbrPoints

    def calculDuree(self, uneVitesse):
        duree =  (self.angleDeFin - self.angleDeDebut) / round(uneVitesse)
        return duree

    def mouvement(self, sens, suite):
        self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, self.angleARepeterCourant)
        if(sens):
            self.etape += 1
            stop = self.nbrPoints
        else:
            self.etape -= 1
            stop = -1

        print("Etape : "+ str(self.etape))

        if(self.etape == stop):
            print(time.time() - self.monTemps)
            self.timer.stop()
            NodeCourant.getInstance().enleverNode(self)
            if(suite == ""):
                self.sortieNode.call()
            else:
                exec(suite)

    def execution(self, sens, paramSuite, etape = -1):
        if(etape == -1):
            if(sens):
                self.etape = 0
                self.objet.Placement.Rotation.Angle = math.radians(self.angleDeDebut)
            else:
                self.etape = self.nbrPoints - 1
                self.objet.Placement.Rotation.Angle = math.radians(self.angleDeFin)
        
        if(sens):
            self.angleARepeterCourant = self.angleARepeter
        else:
            self.angleARepeterCourant = -self.angleARepeter
            
        mouvement = functools.partial(self.mouvement, sens = sens, suite = paramSuite)

        #Bug de timer lorsque le mouvement est un aller boucle, il se mets à avancer de plus en vite
        #Test : Lorsqu'on fait 2 aller à la suite le 2ème est accéléré, pourquoi ?
        NodeCourant.getInstance().ajouterNode(self)
        
        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)

        self.timer.timeout.connect(mouvement)
        self.timer.start()

    def allerALEtape(self, etape):
        deltaEtape = self.etape - etape
        if(deltaEtape >= 0):
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, -self.angleARepeterCourant)
        else:
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, self.angleARepeterCourant)
        self.etape = etape