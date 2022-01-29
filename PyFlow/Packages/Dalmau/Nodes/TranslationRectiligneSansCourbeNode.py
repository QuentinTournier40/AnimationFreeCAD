from PyFlow.Packages.Dalmau.Class.TranslationRectiligneSansCourbe import TranslationRectiligneSansCourbe
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
import FreeCAD

class TranslationRectiligneSansCourbeNode(NodeAnimation):
    
    def __init__(self, name):
        super(TranslationRectiligneSansCourbeNode, self).__init__(name)
        self.createInputPin("Point de depart", "VectorPin")
        self.createInputPin("Point de fin", "VectorPin")

    def execute(self, *args, **kwargs):
        monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        monPointDeDepart = self.getData("Point de depart")
        monPointDeFin = self.getData("Point de fin")
        maDuree = self.getData("Duree deplacement")
        monEstBoucle = self.getData("Boucle")
        monEstAllerRetour = self.getData("Aller-retour")

        translation = TranslationRectiligneSansCourbe(self, monObjet, monPointDeDepart, monPointDeFin, maDuree, monEstBoucle, monEstAllerRetour)
        translation.translater()

    @staticmethod
    def category():
        return 'Translation'

    @staticmethod
    def description():
        return "Fait bouger des bails"