from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
import FreeCAD
import math


class PlacerAngleDunObjet(NodeBase):
    def __init__(self, name):
        super(PlacerAngleDunObjet, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createInputPin("Objet","StringPin")
        self.createInputPin("Angle","FloatPin")
        self.createOutputPin("outExec", "ExecPin")
        self.createOutputPin("Angle de fin","FloatPin")

    def execute(self, *args, **kwargs):
        monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        monObjet.Placement.Rotation.Angle = math.radians(self.getData("Angle"))
        self.setData("Angle de fin", self.getData("Angle"))
        self["outExec"].call()

    @staticmethod
    def category():
        return 'Autre'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Change l'angle de base d'un objet"
