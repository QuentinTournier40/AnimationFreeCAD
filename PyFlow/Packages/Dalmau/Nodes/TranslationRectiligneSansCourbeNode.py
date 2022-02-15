from PyFlow.Packages.Dalmau.Class.TranslationRectiligneSansCourbe import TranslationRectiligneSansCourbe
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from PyFlow.Packages.Dalmau.Class.Mouvement import FenetreErreur
from Qt.QtWidgets import *

import FreeCAD

class TranslationRectiligneSansCourbeNode(NodeAnimation):
    
    def __init__(self, name):
        super(TranslationRectiligneSansCourbeNode, self).__init__(name)
        self.pointDepart = self.createInputPin("Point de depart", "VectorPin")
        self.pointDeFin = self.createInputPin("Point de fin", "VectorPin")        
        self.duree = self.createInputPin("Duree", "FloatPin")

    def compute(self, *args, **kwargs):
        try:
            FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        except IndexError:
            return FenetreErreur("Erreur", self.name, self.objet.name, "Aucun objet ne porte le nom que vous avez saisi.")    

        if(self.duree.getData() <= 0):
            return FenetreErreur("Erreur", self.name, self.duree.name, "La durée ne peut pas être inférieure ou égale à 0.")    
        
        translation = TranslationRectiligneSansCourbe(self)
        translation.translater()

        #self.setData("Position finale", monPointDeFin)

    @staticmethod
    def category():
        return 'Translation'

    @staticmethod
    def description():
        return "Fait bouger des bails"
    
class MainWindow(QMainWindow):
    def init(self):
        QMainWindow.init(self)