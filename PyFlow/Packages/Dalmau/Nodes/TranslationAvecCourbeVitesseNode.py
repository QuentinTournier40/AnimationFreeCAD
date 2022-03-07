from PyFlow.Packages.Dalmau.Class.TranslationAvecCourbe import TranslationAvecCourbe
from PyFlow.Packages.Dalmau.Class.Mouvement import FenetreErreur
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from PyFlow.Packages.Dalmau.Class.Animation import Animation
from Qt.QtWidgets import *

import FreeCAD

class TranslationAvecCourbeVitesseNode(NodeAnimation):
    def __init__(self, name):
        super(TranslationAvecCourbeVitesseNode, self).__init__(name)
        self.nomCourbe = self.createInputPin("Courbe", "StringPin")
        self.vitesse = self.createInputPin("Vitesse", "FloatPin")
    
    def compute(self, *args, **kwargs):
        try:
            objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.objet.getData())[0]
        except IndexError:
            return FenetreErreur("Erreur", self.name, self.objet.name, "Aucun objet ne porte le nom que vous avez saisi.")    
        
        try:
            courbe = FreeCAD.ActiveDocument.getObjectsByLabel(self.nomCourbe.getData())[0]
        except IndexError:
            return FenetreErreur("Erreur", self.name, self.nomCourbe.name, "Aucune courbe ne porte le nom que vous avez saisi.")    

        
        if(self.vitesse.getData() <= 0):
            return FenetreErreur("Erreur", self.name, self.vitesse.name, "La durée ne peut pas être inférieure ou égale à 0.")  

        vitesse = self.vitesse.getData()
        estAllerRetour = self.estAllerRetour.getData()  
        estBoucle = self.estBoucle.getData()
        

        translation = TranslationAvecCourbe(courbe, self)
        animation = Animation(estBoucle, estAllerRetour, self)
        animation.executionVitesse(translation, objet, vitesse)
        
    @staticmethod
    def category():
        return 'Translation|Vitesse'

    @staticmethod
    def description():
        return "Fait bouger des bails en suivant la trajectoire de n'importe quel type de courbe"