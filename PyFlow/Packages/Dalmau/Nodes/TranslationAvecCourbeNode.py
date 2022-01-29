from fnmatch import translate
from PyFlow.Packages.Dalmau.Class.TranslationAvecCourbe import TranslationAvecCourbe
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
import FreeCAD

class TranslationAvecCourbeNode(NodeAnimation):
    
    def __init__(self, name):
        super(TranslationAvecCourbeNode, self).__init__(name)
        self.createInputPin("Courbe", "StringPin")
    
    def execute(self, *args, **kwargs):
        monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        maCourbe = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Courbe"))[0]
        maDuree = self.getData("Duree deplacement")
        monEstBoucle = self.getData("Boucle")
        monEstAllerRetour = self.getData("Aller-retour")

        translation = TranslationAvecCourbe(self, monObjet, maCourbe, maDuree, monEstBoucle, monEstAllerRetour)
        translation.translater()

    @staticmethod
    def category():
        return 'Translation'

    @staticmethod
    def description():
        return "Fait bouger des bails en suivant la trajectoire de n'importe quel type de courbe"
