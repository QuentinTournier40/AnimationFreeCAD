from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Packages.Dalmau.Class.Mouvement import FenetreErreur
from Qt.QtWidgets import *

import FreeCAD

class PlacerNode(NodeBase):
    def __init__(self, name):
        super(PlacerNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.objet = self.createInputPin("Objet","StringPin")
        self.coordonnees = self.createInputPin("Coordonnees","VectorPin")
        self.createOutputPin("outExec", "ExecPin")
        self.createOutputPin("Coordonnees de fin","VectorPin")

    def execute(self, *args, **kwargs):
        try:
            monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        except IndexError:
            return FenetreErreur("Erreur", self.name, self.objet.name, "Aucun objet ne porte le nom que vous avez saisi.")    
        
        monObjet.Placement.Base = self.getData("Coordonnees")
        self.setData("Coordonnees de fin", self.getData("Coordonnees"))
        self["outExec"].call()

    @staticmethod
    def category():
        return 'Placement|Base'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Place un objet aux coordonées données"