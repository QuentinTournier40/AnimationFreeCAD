from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *

import FreeCAD

class PlaceNode(NodeBase):
    def __init__(self, name):
        super(PlaceNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.objet = self.createInputPin("Object","ObjectPin", DEFAULT_VALUE_OBJECT_PIN)
        self.coordonnees = self.createInputPin("Coordinates","VectorPin")
        self.createOutputPin("outExec", "ExecPin")
        self.createOutputPin("End coordinates","VectorPin")
        self.createOutputPin("Object use","ObjectPin", DEFAULT_VALUE_OBJECT_PIN)

    def execute(self, *args, **kwargs):
        if(self.getData("Object") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Error", self.name, self.objet.name, "Please choose an object.")  
        
        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Object"))[0]
        objet.Placement.Base = self.getData("Coordinates")
        self.setData("End coordinates", self.getData("Coordinates"))
        self.setData("Object use", objet.Label)
        self["outExec"].call()

    @staticmethod
    def category():
        return 'en|Placement|Base'

    @staticmethod
    def description():
        return "Places an object at the given coordinates."