from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *

import FreeCAD
from PyFlow.Packages.AnimationFreeCAD.Pins.ObjectPin import ObjectPin

class GetPosition(NodeBase):
    def __init__(self, name):
        super(GetPosition, self).__init__(name)
        self.createInputPin("Object", "ObjectPin")
        self.createOutputPin("Position", "VectorPin")
        
    def compute(self, *args, **kwargs):
      if(self.getData("Object") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Error", self.name, self.objet.name, "Please choose an object.")
      objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Object"))[0]
      self.setData("Position",objet.Placement.Base)

    @staticmethod
    def category():
        return 'en|Placement|Base'

    @staticmethod
    def description():
        return "Return the position of an object."