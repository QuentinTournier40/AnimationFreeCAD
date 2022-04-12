import FreeCAD

from PyFlow.Packages.AnimationFreeCAD.Class.Rotation import Rotation
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.NodeAnimation import NodeAnimation
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from FreeCAD import Vector
from PySide2.QtWidgets import *

class RotationNode(NodeAnimation):
    def __init__(self, name):
        super(RotationNode, self).__init__(name)
        self.createInputPin("Axe de rotation", "VectorPin", Vector(0,0,1))
        self.createInputPin("Centre de rotation", "VectorPin")
        self.createInputPin("Angle au debut de la rotation", "FloatPin")
        self.createInputPin("Angle a la fin de la rotation", "FloatPin")
        self.createOutputPin("Angle final", "FloatPin")
        self.duree = self.createInputPin("Duree", "FloatPin")

    def compute(self, *args, **kwargs):
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")
        if(self.getData("Duree") <= 0):
            return FenetreErreur("Erreur", self.name, self.duree.name, "La durée ne peut pas être inférieure ou égale à 0.")

        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        axeDeRotation = self.getData("Axe de rotation")
        centreDeRotation = self.getData("Centre de rotation")
        angleDeDebut = self.getData("Angle au debut de la rotation")
        angleDeFin = self.getData("Angle a la fin de la rotation")
        duree = self.getData("Duree")

        super().compute()

        self.mouvement = Rotation(axeDeRotation, centreDeRotation, angleDeDebut, angleDeFin,self)
        self.animation.executionDuree(self.mouvement, objet, duree)

        self.setData("Position finale", objet.Placement.Base)
        self.setData("Angle final", angleDeFin)
        self.setData("Objet use", objet.Label)

    @staticmethod
    def category():
        return 'fr|Rotation|Durée'

    @staticmethod
    def description():
        return "Fait tourner des objets."
