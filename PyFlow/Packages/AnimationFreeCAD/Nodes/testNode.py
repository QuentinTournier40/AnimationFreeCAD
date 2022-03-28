import functools
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PySide import QtCore
import FreeCAD


class testNode(NodeBase):
    def __init__(self, name):
        super(testNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createOutputPin("outExec", "ExecPin")

        self.createInputPin("Duree", "FloatPin")

        self.createInputPin("debutAcc", "FloatPin")
        self.createInputPin("FinAcc", "FloatPin")

        self.createInputPin("vitesseInit", "FloatPin")
        self.createInputPin("Acc", "FloatPin")

        self.createInputPin("Courbe", "CurvePin", "---Select object---")
        self.createInputPin("Objet", "ObjectPin", "---Select object---")


    def execute(self, *args, **kwargs):
        self.duree = self.getData("Duree")
        self.debutAcc = self.getData("debutAcc")
        self.finAcc = self.getData("FinAcc")

        self.vitesseInit = self.getData("vitesseInit")

        self.acc = self.getData("Acc") /100
        self.compteur = 0
        self.distanceParcourue = 0

        self.courbe = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Courbe"))[0]
        self.objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]

        self.distanceParcourue2 = []
        self.temps = []
        self.distanceParcourue2.append(0)
        self.distanceParcourue2.append(0)
        self.temps.append(0)
        self.temps.append(0)

        self.delta = self.finAcc - self.debutAcc

        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)

        mouvement = functools.partial(self.truc)

        self.timer.timeout.connect(mouvement)
        self.timer.start()
        self.mouvementEstAccelere = False

    def truc(self):
        #print("Temps : " + str(self.compteur))
        #print("Distance Parcourue : " + str(self.distanceParcourue))

        if(self.distanceParcourue < self.debutAcc):
            self.distanceParcourue = self.calculDistance(False)  
            self.distanceParcourue2[0] = self.distanceParcourue
            self.temps[0] = self.compteur

        if((self.distanceParcourue >= self.debutAcc) and (self.distanceParcourue < self.finAcc)):
            self.distanceParcourue = 1/2 * self.acc * ((self.compteur - self.temps[0]) * (self.compteur - self.temps[0])) + self.vitesseInit * (self.compteur -self.temps[0]) + self.distanceParcourue2[0]
            self.distanceParcourue2[1] = self.distanceParcourue
            self.temps[1] = self.compteur

        elif(self.distanceParcourue >= self.finAcc):
            #print("3")
            self.distanceParcourue = self.vitesseInit * (self.compteur - self.temps[1]) + self.distanceParcourue2[1]
            
            if(self.distanceParcourue > self.courbe.Shape.LastParameter):
                #print("fin")
                self.timer.stop()

        self.objet.Placement.Base = self.courbe.Shape.valueAt(self.distanceParcourue)
        self.compteur += 0.02

    def calculDistance(self, estAccelere):
        dist = self.vitesseInit * self.compteur
        return dist

    @staticmethod
    def category():
        return 'Autre'

    @staticmethod
    def description():
        return "Lance plusieurs node en meme temps"