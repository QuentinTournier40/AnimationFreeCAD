from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Packages.Dalmau.Class.Mouvement import *

import FreeCAD
import math

class setAngleObjectNode(NodeBase):
    def __init__(self, name):
        super(setAngleObjectNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.objet = self.createInputPin("Objet","ObjectPin", DEFAULT_VALUE_OBJECT_PIN)
        self.createInputPin("Angle","FloatPin")
        self.createOutputPin("outExec", "ExecPin")
        self.createOutputPin("Angle de fin","FloatPin")
        self.createOutputPin("Objet use","ObjectPin")

    def execute(self, *args, **kwargs):
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")  
        
        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        angle = self.getData("Angle")
        objet.Placement.Rotation.Angle = math.radians(angle)
        
        self.setData("Angle de fin", angle)
        self.setData("Objet use", objet.Label)
        
        self["outExec"].call()

    @staticmethod
    def category():
        return 'Placement|Angle'

    @staticmethod
    def description():
        return "Change l'angle de base d'un objet"