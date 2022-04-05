from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from PyFlow.Packages.AnimationFreeCAD.Class.FenetreErreur import FenetreErreur

import FreeCAD

class GetPlacement(NodeBase):
    def __init__(self, name):
        super(GetPlacement, self).__init__(name)
        self.createInputPin("Objet", "ObjectPin")
        self.createOutputPin("Position", "VectorPin")
        
    def compute(self, *args, **kwargs):
      if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")
      objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
      self.setData("Position",objet.Placement.Base)

    @staticmethod
    def category():
        return 'fr|Placement|Base'

    @staticmethod
    def description():
        return "Retourne le placement d'un objet."