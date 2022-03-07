from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Packages.Dalmau.Class.Mouvement import FenetreErreur
from Qt.QtWidgets import *

import FreeCAD
import math


class setAngleObjectNode(NodeBase):
    def __init__(self, name):
        super(setAngleObjectNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.objet = self.createInputPin("Objet","StringPin")
        self.angle = self.createInputPin("Angle","FloatPin")
        self.createOutputPin("outExec", "ExecPin")
        self.createOutputPin("Angle de fin","FloatPin")

    def execute(self, *args, **kwargs):
        try:
            monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        except IndexError:
            return FenetreErreur("Erreur", self.name, self.objet.name, "Aucun objet ne porte le nom que vous avez saisi.")    

        monObjet.Placement.Rotation.Angle = math.radians(self.getData("Angle"))
        self.setData("Angle de fin", self.getData("Angle"))
        self["outExec"].call()

    @staticmethod
    def category():
        return 'Placement|Angle'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Change l'angle de base d'un objet"