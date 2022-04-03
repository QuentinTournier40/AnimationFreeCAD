from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from PyFlow.Packages.AnimationFreeCAD.Class.MouvementEnCours import MouvementEnCours
from PySide import QtCore

import functools
import time
import math

from math import *


class Rotation2(Mouvement):

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
        duree = (self.angleDeFin - self.angleDeDebut) / round(uneVitesse)
        return duree

    def mouvement(self, sens, suite):     
        m = self.objet.Placement.Rotation.Matrix
        m.rotateX(math.radians(self.angleARepeter) * self.axeDeRotation.x)
        m.rotateY(math.radians(self.angleARepeter) * self.axeDeRotation.y)
        m.rotateZ(math.radians(self.angleARepeter) * self.axeDeRotation.z)
        q = self.matrixToQ(m)
        self.objet.Placement.Rotation = q
        if(sens):
            self.etape += 1
            stop = self.nbrPoints
        else:
            self.etape -= 1
            stop = -1

        #print("Etape : "+ str(self.etape))

        if(self.etape == stop):
            #print(time.time() - self.monTemps)
            
            self.timer.stop()
            MouvementEnCours.getInstance().enleverNode(self)
            if(suite == ""):
                self.sortieNode.call()
            else:
                exec(suite)

    def execution(self, sens, paramSuite, etape=-1):
        if(etape == -1):
            if(sens):
                self.etape = 0
                m = self.objet.Placement.Rotation.Matrix
                m.rotateX(math.radians(self.angleDeDebut) * self.axeDeRotation.x)
                m.rotateY(math.radians(self.angleDeDebut) * self.axeDeRotation.y)
                m.rotateZ(math.radians(self.angleDeDebut) * self.axeDeRotation.z)
                q = self.matrixToQ(m)
                self.objet.Placement.Rotation = q
            else:
                self.etape = self.nbrPoints - 1
                m = self.objet.Placement.Rotation.Matrix
                m.rotateX(math.radians(self.angleDeFin) * self.axeDeRotation.x)
                m.rotateY(math.radians(self.angleDeFin) * self.axeDeRotation.y)
                m.rotateZ(math.radians(self.angleDeFin) * self.axeDeRotation.z)
                q = self.matrixToQ(m)
                self.objet.Placement.Rotation = q
        if(sens):
            self.angleARepeterCourant = self.angleARepeter
        else:
            self.angleARepeterCourant = -self.angleARepeter

        mouvement = functools.partial(self.mouvement, sens=sens, suite=paramSuite)

        # Bug de timer lorsque le mouvement est un aller boucle, il se mets à avancer de plus en vite
        # Test : Lorsqu'on fait 2 aller à la suite le 2ème est accéléré, pourquoi ?
        MouvementEnCours.getInstance().ajouterNode(self)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)

        self.timer.timeout.connect(mouvement)
        self.timer.start()

    def allerALEtape(self, etape):
        deltaEtape = self.etape - etape
        if(deltaEtape >= 0):
            self.objet.Placement.rotate(
                self.centreDeRotation, self.axeDeRotation, -self.angleARepeterCourant)
        else:
            self.objet.Placement.rotate(
                self.centreDeRotation, self.axeDeRotation, self.angleARepeterCourant)
            self.etape = etape
            
    def getTrace(self, m):
        trace = m.A11 + m.A22 + m.A33 + m.A44
        return trace

    def matrixToQ(self, m):
        """https://jeux.developpez.com/faq/math/?page=quaternions"""
        trace = self.getTrace(m)
        if(trace > 0 ):
            s = 0.5/sqrt(trace)
            x = (m.A32 - m.A23) * s
            y = (m.A13 - m.A31) * s
            z = (m.A21 - m.A12) * s
            w = 0.25/s
        else:
            if(m.A11 >= m.A22 and m.A11 >= m.A33):
                s = sqrt(m.A44 + m.A11 - m.A22 - m.A33) * 2
                x = 0.25 * s
                y = (m.A12 + m.A21)/s
                z = (m.A13 + m.A31)/s
                w = (m.A32 - m.A23)/s
            elif(m.A22 >= m.A11 and m.A22 >= m.A33):
                s = sqrt(m.A44 - m.A11 + m.A22 - m.A33) * 2
                x = (m.A12 + m.A21)/s
                y = 0.25 * s
                z = (m.A23 + m.A32)/s
                w = (m.A13 - m.A31)/s
            elif(m.A33 >= m.A11 and m.A33 >= m.A22):
                s = sqrt(m.A44 - m.A11 - m.A22 + m.A33) * 2
                x = (m.A13 + m.A31)/s
                y = (m.A23 + m.A32)/s
                z = 0.25 * s
                w = (m.A21 - m.A12)/s
        return (x,y,z,w)    
