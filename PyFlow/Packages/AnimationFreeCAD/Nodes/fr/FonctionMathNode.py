from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.NodeAnimation import NodeAnimation
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from PyFlow.Packages.AnimationFreeCAD.Class.FenetreErreur import FenetreErreur
from PyFlow.Packages.AnimationFreeCAD.Class.translationFormuleMathematiques import translationFormuleMathematiques

import FreeCAD

class FonctionMathNode(NodeAnimation):
    def __init__(self,name):
        super(FonctionMathNode,self).__init__(name)
        self.createInputPin("equation en x","StringPin", "t*t+48")
        self.createInputPin("equation en y","StringPin", "t*t+48")
        self.createInputPin("equation en z","StringPin", "t*t+48")
        self.duree = self.createInputPin("Duree","FloatPin")
        self._experimental = True

    def compute(self, *args, **kwargs):
        super().compute()
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")  
        if(self.getData("Duree") <= 0):
            return FenetreErreur("Erreur", self.name, self.duree.name, "La durée ne peut pas être inférieure ou égale à 0.")

        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        equationX = self.getData("equation en x")
        equationY = self.getData("equation en y")
        equationZ = self.getData("equation en z")
        duree = self.getData("Duree")
        
        self.mouvement = translationFormuleMathematiques(equationX, equationY, equationZ, self)
        self.animation.executionDuree(self.mouvement, objet, duree)

    @staticmethod
    def category():
        return 'fr|Translation|Experimental'

    @staticmethod
    def description():
        return "Fait suivre à un objet des déplacements"