from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *

import FreeCAD
import math

class setAngleObjectNode(NodeBase):
    def __init__(self, name):
        super(setAngleObjectNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.objet = self.createInputPin("Object","ObjectPin", DEFAULT_VALUE_OBJECT_PIN)
        self.createInputPin("Angle","FloatPin")
        self.createOutputPin("outExec", "ExecPin")
        self.createOutputPin("End angle","FloatPin")
        self.createOutputPin("Object use","ObjectPin")

    def execute(self, *args, **kwargs):
        if(self.getData("Object") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Error", self.name, self.objet.name, "Please choose an object.")  
        
        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Object"))[0]
        angle = self.getData("Angle")
        objet.Placement.Rotation.Angle = math.radians(angle)
        
        self.setData("End angle", angle)
        self.setData("Object use", objet.Label)
        
        self["outExec"].call()

    @staticmethod
    def category():
        return 'en|Placement|Angle'

    @staticmethod
    def description():
        return "Changes the base angle of an object"