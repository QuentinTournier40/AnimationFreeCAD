from PyFlow.Packages.Dalmau.Class.Animation import Animation
from PyFlow.Packages.Dalmau.Class.TranslationSansCourbe import TranslationSansCourbe
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from PyFlow.Packages.Dalmau.Class.Mouvement import FenetreErreur
from Qt.QtWidgets import *

import FreeCAD

class TranslationRectiligneVitesseNode(NodeAnimation):
    def __init__(self, name):
        super(TranslationRectiligneVitesseNode, self).__init__(name)
        self.pointDepart = self.createInputPin("Point de depart", "VectorPin")
        self.pointDeFin = self.createInputPin("Point de fin", "VectorPin")        
        self.vitesse = self.createInputPin("Vitesse", "FloatPin")

    def compute(self, *args, **kwargs):
        try:
            objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        except IndexError:
            return FenetreErreur("Erreur", self.name, self.objet.name, "Aucun objet ne porte le nom que vous avez saisi.")    
        
        vitesse = self.vitesse.getData()
        if(vitesse <= 0):
            return FenetreErreur("Erreur", self.name, self.vitesse.name, "La durée ne peut pas être inférieure ou égale à 0.") 

        coordonnes = [self.pointDepart.getData(), self.pointDeFin.getData()] 
        estBoucle = self.estBoucle.getData()
        estAllerRetour = self.estAllerRetour.getData()
        
        translation = TranslationSansCourbe(coordonnes, self)
        animation = Animation(estBoucle, estAllerRetour, self)
        animation.executionVitesse(translation, objet, vitesse)

        self.setData("Position finale", self.pointDeFin.getData())

    @staticmethod
    def category():
        return 'Translation|Vitesse'

    @staticmethod
    def description():
        return "Fait bouger des bails"