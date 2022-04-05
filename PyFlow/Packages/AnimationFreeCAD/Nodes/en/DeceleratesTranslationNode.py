import functools
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PySide import QtCore
import FreeCAD


class DeceleratesTranslationNode(NodeBase):
    def __init__(self, name):
        super(DeceleratesTranslationNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createOutputPin("outExec", "ExecPin")

        self.createInputPin("Initial speed", "FloatPin")
        self.createInputPin("Acceleration", "FloatPin")

        self.createInputPin("Curve", "CurvePin", "---Select object---")
        self.createInputPin("Object", "ObjectPin", "---Select object---")
        self._experimental = True

    def execute(self, *args, **kwargs):
        self.vitesseInit = self.getData("Initial speed")
        self.acc = self.getData("Acceleration")

        self.compteur = 0

        self.courbe = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Curve"))[0]
        self.objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Object"))[0]

        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)

        mouvement = functools.partial(self.mouvementDeceleration)

        self.timer.timeout.connect(mouvement)
        self.timer.start()

    def mouvementDeceleration(self):
        distance = - (1 / 2 * self.acc * (self.compteur * self.compteur)) + self.vitesseInit * self.compteur
        #print("Temps : " + str(self.compteur))
        #print("Distance Parcourue : " + str(distance))
        if(distance > self.courbe.Shape.LastParameter):
            distance = self.courbe.Shape.LastParameter
            self.timer.stop()
        self.objet.Placement.Base = self.courbe.Shape.valueAt(distance)
        self.compteur += 0.032

    @staticmethod
    def category():
        return 'en|Translation|Experimental'

    @staticmethod
    def description():
        return "Decelerates an object."