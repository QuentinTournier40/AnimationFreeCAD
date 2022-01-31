from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
import FreeCAD


class PlacerNode(NodeBase):
    def __init__(self, name):
        super(PlacerNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createInputPin("Objet","StringPin")
        self.createInputPin("Coordonnees","VectorPin")
        self.createOutputPin("outExec", "ExecPin")
        self.createOutputPin("Coordonnees de fin","VectorPin")

    def execute(self, *args, **kwargs):
        monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        monObjet.Placement.Base = self.getData("Coordonnees")
        self.setData("Coordonnees de fin", self.getData("Coordonnees"))
        self["outExec"].call()

    @staticmethod
    def category():
        return 'Autre'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Place un objet au coordonées données"
