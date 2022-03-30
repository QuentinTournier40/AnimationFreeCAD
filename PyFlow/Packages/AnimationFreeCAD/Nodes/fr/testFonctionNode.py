from PyFlow.Packages.AnimationFreeCAD.Class.Animation import Animation
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.NodeAnimation import NodeAnimation
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from PyFlow.Packages.AnimationFreeCAD.Class.translationFormuleMathematiques import translationFormuleMathematiques

import FreeCAD

class testFonctionNode(NodeAnimation):
    def __init__(self,name):
        super(testFonctionNode,self).__init__(name)
        self.createInputPin("equation en x","StringPin")
        self.createInputPin("equation en y","StringPin")
        self.createInputPin("equation en z","StringPin")
        self.duree = self.createInputPin("Duree","FloatPin")

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
        self.animation.executionDuree(self.mouvement, objet, duree)    #lance le timer qui gère l'exécution

    @staticmethod
    def category():
        return 'fr|Autre'

    @staticmethod
    def description():
        return "Fait suivre à un objet des déplacements"