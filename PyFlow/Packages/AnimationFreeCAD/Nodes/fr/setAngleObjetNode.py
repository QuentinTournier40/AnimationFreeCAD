import FreeCAD
import math

from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from PyFlow.Packages.AnimationFreeCAD.Class.FenetreErreur import FenetreErreur
from FreeCAD import Vector

class setAngleObjetNode(NodeBase):
    def __init__(self, name):
        super(setAngleObjetNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.objet = self.createInputPin("Objet","ObjectPin", DEFAULT_VALUE_OBJECT_PIN)
        self.createInputPin("Axe de rotation", "VectorPin", Vector(0,0,1))
        self.createInputPin("Angle","FloatPin")
        
        self.createOutputPin("outExec", "ExecPin")
        self.createOutputPin("Objet use","ObjectPin")
        self.createOutputPin("Axe de rotation de fin","VectorPin")
        self.createOutputPin("Angle de fin","FloatPin")

    def execute(self, *args, **kwargs):
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")  
        
        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        axeDeRotation = self.getData("Axe de rotation")
        angle = self.getData("Angle")
        objet.Placement.Rotation.Axis = axeDeRotation
        objet.Placement.Rotation.Angle = math.radians(angle)
        
        self.setData("Angle de fin", angle)
        self.setData("Objet use", objet.Label)
        self.setData("Axe de rotation de fin", axeDeRotation)
        
        self["outExec"].call()

    @staticmethod
    def category():
        return 'fr|Placement|Angle'

    @staticmethod
    def description():
        return "Change l'angle de base d'un objet"