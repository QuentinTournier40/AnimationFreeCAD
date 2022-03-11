from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Packages.Dalmau.Class.Mouvement import *

import FreeCAD

class PlacerNode(NodeBase):
    def __init__(self, name):
        super(PlacerNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.objet = self.createInputPin("Objet","ObjectPin", DEFAULT_VALUE_OBJECT_PIN)
        self.coordonnees = self.createInputPin("Coordonnees","VectorPin")
        self.createOutputPin("outExec", "ExecPin")
        self.createOutputPin("Coordonnees de fin","VectorPin")
        self.createOutputPin("Objet use","ObjectPin", DEFAULT_VALUE_OBJECT_PIN)

    def execute(self, *args, **kwargs):
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")  
        
        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        objet.Placement.Base = self.getData("Coordonnees")
        self.setData("Coordonnees de fin", self.getData("Coordonnees"))
        self.setData("Objet use", objet.Label)
        self["outExec"].call()

    @staticmethod
    def category():
        return 'Placement|Base'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Place un objet aux coordonées données."