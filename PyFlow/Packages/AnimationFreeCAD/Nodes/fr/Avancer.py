from PyFlow.Packages.AnimationFreeCAD.Class.Animation import Animation
from PyFlow.Packages.AnimationFreeCAD.Class.TranslationSansCourbe import TranslationSansCourbe
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.NodeAnimation import NodeAnimation
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *

import FreeCAD

class AvancerNode(NodeAnimation):
    def __init__(self, name):
        super(AvancerNode, self).__init__(name)
        self.createInputPin("Point de depart", "VectorPin")
        self.createInputPin("Avancement", "VectorPin")        
        self.duree = self.createInputPin("Duree", "FloatPin")

    def compute(self, *args, **kwargs):
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")  
        if(self.getData("Duree") <= 0):
            return FenetreErreur("Erreur", self.name, self.duree.name, "La durée ne peut pas être inférieure ou égale à 0.")

        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        coordonnes = [self.getData("Point de depart"), self.getData("Point de depart") + self.getData("Avancement") ]
        duree = self.getData("Duree")
        
        super().compute()        

        self.mouvement = TranslationSansCourbe(coordonnes, self)
        self.animation.executionDuree(self.mouvement, objet, duree)

        self.setData("Objet use", objet.Label)

    @staticmethod
    def category():
        return 'fr|Translation|Durée'

    @staticmethod
    def description():
        return "Fait bouger des objets entre deux points donnés"