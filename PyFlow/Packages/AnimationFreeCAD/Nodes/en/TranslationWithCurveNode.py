from PyFlow.Packages.AnimationFreeCAD.Class.TranslationAvecCourbe import TranslationAvecCourbe
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.NodeAnimation import NodeAnimation
from PyFlow.Packages.AnimationFreeCAD.Class.Animation import Animation

import FreeCAD

class TranslationWithCurveNode(NodeAnimation):
    def __init__(self, name):
        super(TranslationWithCurveNode, self).__init__(name)
        self.courbe = self.createInputPin("Curve", "CurvePin", DEFAULT_VALUE_OBJECT_PIN)
        self.duree = self.createInputPin("Duration", "FloatPin")
    
    def compute(self, *args, **kwargs):
        if(self.getData("Object") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Error", self.name, self.objet.name, "Please choose an object.")
        if(self.getData("Curve") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Error", self.name, self.courbe.name, "Please choose a curve.")  
        if(self.getData("Duration") <= 0):
            return FenetreErreur("Error", self.name, self.duree.name, "Duration cannot be less than or equal to 0.")

        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Object"))[0]
        courbe = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Curve"))[0]
        duree = self.getData("Duration")
        
        super().compute() 
        
        self.mouvement = TranslationAvecCourbe(courbe, self)
        self.animation.executionDuree(self.mouvement, objet, duree)

        self.setData("Final position", objet.Placement.Base)
        self.setData("Object use", objet.Label)
        
    @staticmethod
    def category():
        return 'en|Translation|Duration'

    @staticmethod
    def description():
        return "Moves objects along a curve at uniform speed."