import functools
import FreeCAD

from PyFlow.Core import NodeBase
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from PyFlow.Packages.AnimationFreeCAD.Class.FenetreErreur import FenetreErreur

from PySide import QtCore

class TranslationAccelere(NodeBase):
    def __init__(self, name):
        super(TranslationAccelere, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createOutputPin("outExec", "ExecPin")

        self.createInputPin("Objet", "ObjectPin", DEFAULT_VALUE_OBJECT_PIN)
        self.createInputPin("Courbe", "CurvePin", DEFAULT_VALUE_OBJECT_PIN)

        self.createInputPin("vitesseInit", "FloatPin")
        self.createInputPin("Acc", "FloatPin")
        self._experimental = True

    def execute(self, *args, **kwargs):
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")
        if(self.getData("Courbe") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.courbe.name, "Veuillez choisir une courbe à suivre.")  


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
        self.compteur += NOMBRE_D_OR / 1000

    @staticmethod
    def category():
        return 'fr|Translation|Experimental'

    @staticmethod
    def description():
        return "Accelere un objet."