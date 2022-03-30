from PyFlow.Packages.AnimationFreeCAD.Class.Animation import Animation
from PyFlow.Packages.AnimationFreeCAD.Class.TranslationSansCourbe import TranslationSansCourbe
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.NodeAnimation import NodeAnimation
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *

import FreeCAD

class RectilinearTranslationNode(NodeAnimation):
    def __init__(self, name):
        super(RectilinearTranslationNode, self).__init__(name)
        self.createInputPin("Starting point", "VectorPin")
        self.createInputPin("End point", "VectorPin")        
        self.duree = self.createInputPin("Duration", "FloatPin")

    def compute(self, *args, **kwargs):
        if(self.getData("Object") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Error", self.name, self.objet.name, "Please choose an object.")  
        if(self.getData("Duration") <= 0):
            return FenetreErreur("Error", self.name, self.duree.name, "Duration cannot be less than or equal to 0.")

        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Object"))[0]
        coordonnes = [self.getData("Starting point"), self.getData("End point")]
        duree = self.getData("Duration")
        
        super().compute()        

        self.mouvement = TranslationSansCourbe(coordonnes, self)
        self.animation.executionDuree(self.mouvement, objet, duree)

        self.setData("Final position", self.getData("End point"))
        self.setData("Object use", objet.Label)

    @staticmethod
    def category():
        return 'en|Translation|Duration'

    @staticmethod
    def description():
        return "Moves objects between two given points"