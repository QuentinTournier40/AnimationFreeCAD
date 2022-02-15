from PyFlow.Packages.Dalmau.Class.TranslationAvecCourbe import TranslationAvecCourbe
from PyFlow.Packages.Dalmau.Class.Mouvement import FenetreErreur
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from Qt.QtWidgets import *

import FreeCAD

class TranslationAvecCourbeNode(NodeAnimation):
    def __init__(self, name):
        super(TranslationAvecCourbeNode, self).__init__(name)
        self.nomCourbe = self.createInputPin("Courbe", "StringPin")
        self.duree = self.createInputPin("Duree", "FloatPin")
    
    def compute(self, *args, **kwargs):
        try:
            FreeCAD.ActiveDocument.getObjectsByLabel(self.objet.getData())[0]
        except IndexError:
            return FenetreErreur("Erreur", self.name, self.objet.name, "Aucun objet ne porte le nom que vous avez saisi.")    
        
        try:
            self.courbe = FreeCAD.ActiveDocument.getObjectsByLabel(self.nomCourbe.getData())[0]
        except IndexError:
            return FenetreErreur("Erreur", self.name, self.nomCourbe.name, "Aucune courbe ne porte le nom que vous avez saisi.")    

        
        if(self.duree.getData() <= 0):
            return FenetreErreur("Erreur", self.name, self.duree.name, "La durée ne peut pas être inférieure ou égale à 0.")    

        translation = TranslationAvecCourbe(self)
        translation.translater()
        
    @staticmethod
    def category():
        return 'Translation'

    @staticmethod
    def description():
        return "Fait bouger des bails en suivant la trajectoire de n'importe quel type de courbe"