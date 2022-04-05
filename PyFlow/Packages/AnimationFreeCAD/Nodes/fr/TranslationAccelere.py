from dis import dis
import functools
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PySide import QtCore
import FreeCAD


class TranslationAccelere(NodeBase):
    def __init__(self, name):
        super(TranslationAccelere, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createOutputPin("outExec", "ExecPin")

        self.createInputPin("vitesseInit", "FloatPin")
        self.createInputPin("Acc", "FloatPin")

        self.createInputPin("Courbe", "CurvePin", "---Select object---")
        self.createInputPin("Objet", "ObjectPin", "---Select object---")
        self._experimental = True

    def execute(self, *args, **kwargs):
        self.vitesseInit = self.getData("vitesseInit")
        self.acc = self.getData("Acc")

        self.compteur = 0

        self.courbe = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Courbe"))[0]
        self.objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]

        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)

        mouvement = functools.partial(self.mouvementAcceleration)

        self.timer.timeout.connect(mouvement)
        self.timer.start()

    def mouvementAcceleration(self):
        distance = 1 / 2 * self.acc * (self.compteur * self.compteur) + self.vitesseInit * self.compteur
        if(distance > self.courbe.Shape.LastParameter):
            distance = self.courbe.Shape.LastParameter
            self.timer.stop()
        self.objet.Placement.Base = self.courbe.Shape.valueAt(distance)
        self.compteur += 0.032

    @staticmethod
    def category():
        return 'fr|Translation|Experimental'

    @staticmethod
    def description():
        return "Accelere un objet."