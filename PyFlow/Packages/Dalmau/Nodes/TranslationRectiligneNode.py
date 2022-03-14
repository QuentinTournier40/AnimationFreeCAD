from PyFlow.Packages.Dalmau.Class.Animation import Animation
from PyFlow.Packages.Dalmau.Class.TranslationSansCourbe import TranslationSansCourbe
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from PyFlow.Packages.Dalmau.Class.Mouvement import *

import FreeCAD

class TranslationRectiligneNode(NodeAnimation):
    def __init__(self, name):
        super(TranslationRectiligneNode, self).__init__(name)
        self.createInputPin("Point de depart", "VectorPin")
        self.createInputPin("Point de fin", "VectorPin")        
        self.duree = self.createInputPin("Duree", "FloatPin")

    def compute(self, *args, **kwargs):
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")  
        if(self.getData("Duree") <= 0):
            return FenetreErreur("Erreur", self.name, self.duree.name, "La durée ne peut pas être inférieure ou égale à 0.")

        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        coordonnes = [self.getData("Point de depart"), self.getData("Point de fin")]
        duree = self.getData("Duree")
        
        super().compute()        

        self.mouvement = TranslationSansCourbe(coordonnes, self)
        self.animation.executionDuree(self.mouvement, objet, duree)

        self.setData("Position finale", self.getData("Point de fin"))
        self.setData("Objet use", objet.Label)

    @staticmethod
    def category():
        return 'Translation|Durée'

    @staticmethod
    def description():
        return "Fait bouger des objets entre deux points donnés"