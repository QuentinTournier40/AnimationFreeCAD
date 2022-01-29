from PyFlow.Packages.Dalmau.Class.TranslationRectiligneSansCourbe import TranslationRectiligneSansCourbe
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
import FreeCAD

class TranslationRectiligneSansCourbeNode(NodeAnimation):
    
    def __init__(self, name):
        super(TranslationRectiligneSansCourbeNode, self).__init__(name)
        self.createInputPin("X point de depart", "FloatPin")
        self.createInputPin("Y point de depart", "FloatPin")
        self.createInputPin("Z point de depart", "FloatPin")
        self.createInputPin("X point de fin", "FloatPin")
        self.createInputPin("Y point de fin", "FloatPin")
        self.createInputPin("Z point de fin", "FloatPin")

    def compute(self, *args, **kwargs):
        monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        monPointDeDepart = FreeCAD.Vector(self.getData("X point de depart"), self.getData("Y point de depart"), self.getData("Z point de depart"))
        monPointDeFin = FreeCAD.Vector(self.getData("X point de fin"), self.getData("Y point de fin"), self.getData("Z point de fin"))
        maDuree = self.getData("Duree deplacement")
        monEstBoucle = self.getData("Realiser en boucle ?")
        monEstAllerRetour = self.getData("Realiser en aller-retour")

        translation = TranslationRectiligneSansCourbe(self, monObjet, monPointDeDepart, monPointDeFin, maDuree, monEstBoucle, monEstAllerRetour)
        translation.translater()

    @staticmethod
    def category():
        return 'Translation'

    @staticmethod
    def description():
        return "Fait bouger des bails"