from PyFlow.Packages.Dalmau.Class.Mouvement import *
from PyFlow.Packages.Dalmau.Class.NodeCourant import NodeCourant
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

    def setObjet(self, objet):
        self.objet = objet

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
            exec(suite)   

    def execution(self, sens, paramSuite):
        if(sens):
            self.etape = 0
            self.objet.Placement.Rotation.Angle = math.radians(self.angleDeDebut)
            mouvement = functools.partial(self.mouvement, sens = True, suite = paramSuite)
            self.angleARepeterCourant = self.angleARepeter
        else:
            self.etape = self.nbrPoints - 1
            self.objet.Placement.Rotation.Angle = math.radians(self.angleDeFin)
            self.angleARepeterCourant = -self.angleARepeter
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
        deltaEtape = self.etape - etape
        angle = self.objet.Placement.Rotation.Angle
        nouvelleAngle = angle + self.angleARepeter * deltaEtape
        self.objet.Placement.Rotation.Angle = nouvelleAngle
        self.etape = etape