from PyFlow.Packages.AnimationFreeCAD.Class.Animation import Animation
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.NodeAnimation import NodeAnimation
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from PyFlow.Packages.AnimationFreeCAD.Class.translationFormuleMathematiques import translationFormuleMathematiques

import FreeCAD

class MathTranslation(NodeAnimation):
    def __init__(self,name):
        super(MathTranslation,self).__init__(name)
        self.createInputPin("equation in x","StringPin")
        self.createInputPin("equation in y","StringPin")
        self.createInputPin("equation in z","StringPin")
        self.duree = self.createInputPin("Duration","FloatPin")
        self._experimental = True

    def compute(self, *args, **kwargs):
        super().compute()
        if(self.getData("Object") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Error", self.name, self.objet.name, "Please choose an object.")  
        if(self.getData("Duration") <= 0):
            return FenetreErreur("Error", self.name, self.duree.name, "Duration cannot be less than or equal to 0.")

        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Object"))[0]
        equationX = self.getData("equation in x")
        equationY = self.getData("equation in y")
        equationZ = self.getData("equation in z")
        duree = self.getData("Duration")
        
        self.mouvement = translationFormuleMathematiques(equationX, equationY, equationZ, self)
        self.animation.executionDuree(self.mouvement, objet, duree)    #lance le timer qui gère l'exécution

    @staticmethod
    def category():
        return 'en|Translation|Experimental'

    @staticmethod
    def description():
        return "Makes an object follow movements."