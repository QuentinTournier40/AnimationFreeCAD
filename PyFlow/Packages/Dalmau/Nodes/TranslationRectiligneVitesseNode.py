from PyFlow.Packages.Dalmau.Class.Animation import Animation
from PyFlow.Packages.Dalmau.Class.TranslationSansCourbe import TranslationSansCourbe
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from PyFlow.Packages.Dalmau.Class.Mouvement import *

import FreeCAD

class TranslationRectiligneVitesseNode(NodeAnimation):
    def __init__(self, name):
        super(TranslationRectiligneVitesseNode, self).__init__(name)
        self.createInputPin("Point de depart", "VectorPin")
        self.createInputPin("Point de fin", "VectorPin")        
        self.vitesse = self.createInputPin("Vitesse", "FloatPin")

    def compute(self, *args, **kwargs):
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")
        if(self.getData("Vitesse") <= 0):
            return FenetreErreur("Erreur", self.name, self.vitesse.name, "La vitesse ne peut pas être inférieure ou égale à 0.")
        
        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        coordonnes = [self.getData("Point de depart"), self.getData("Point de fin")] 
        vitesse = self.getData("Vitesse")
        estBoucle = self.getData("Boucle")
        estAllerRetour = self.getData("Aller-retour")
        
        self.mouvement = TranslationSansCourbe(coordonnes, self)
        animation = Animation(estBoucle, estAllerRetour, self)
        animation.executionVitesse(self.mouvement, objet, vitesse)

        self.setData("Position finale", self.getData("Point de fin"))
        self.setData("Objet use", objet.Label)

    @staticmethod
    def category():
        return 'Translation|Vitesse'

    @staticmethod
    def description():
        return "Fait bouger des objets entre deux points donnés"