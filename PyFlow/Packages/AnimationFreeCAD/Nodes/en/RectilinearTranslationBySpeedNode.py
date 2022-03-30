from PyFlow.Packages.AnimationFreeCAD.Class.Animation import Animation
from PyFlow.Packages.AnimationFreeCAD.Class.TranslationSansCourbe import TranslationSansCourbe
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.NodeAnimation import NodeAnimation
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *

import FreeCAD

class RectilinearTranslationBySpeedNode(NodeAnimation):
    def __init__(self, name):
        super(RectilinearTranslationBySpeedNode, self).__init__(name)
        self.createInputPin("Starting point", "VectorPin")
        self.createInputPin("End point", "VectorPin")        
        self.vitesse = self.createInputPin("Speed", "FloatPin")

    def compute(self, *args, **kwargs):
        if(self.getData("Object") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Error", self.name, self.objet.name, "Please choose an object.")
        if(self.getData("Speed") <= 0):
            return FenetreErreur("Error", self.name, self.vitesse.name, "Speed cannot be less than or equal to 0.")
        
        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Object"))[0]
        coordonnes = [self.getData("Starting point"), self.getData("End point")] 
        vitesse = self.getData("Speed")
        
        super().compute()        
        
        self.mouvement = TranslationSansCourbe(coordonnes, self)
        self.animation.executionVitesse(self.mouvement, objet, vitesse)

        self.setData("Final position", self.getData("End point"))
        self.setData("Object use", objet.Label)

    @staticmethod
    def category():
        return 'en|Translation|Speed'

    @staticmethod
    def description():
        return "Moves objects between two given points"