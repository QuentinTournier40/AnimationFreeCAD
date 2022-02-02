from PyFlow.Packages.Dalmau.Class.TranslationRectiligneSansCourbe import TranslationRectiligneSansCourbe
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from Qt.QtWidgets import *

import FreeCAD

class TranslationRectiligneSansCourbeNode(NodeAnimation):
    
    def __init__(self, name):
        super(TranslationRectiligneSansCourbeNode, self).__init__(name)
        self.createInputPin("Point de depart", "VectorPin")
        self.createInputPin("Point de fin", "VectorPin")

    def compute(self, *args, **kwargs):
        try:
            monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        except IndexError:
            w = MainWindow()
            msg = QMessageBox()
            titre = "Erreur"
            texte = "Erreur au node " + self.name + ": \nPin : " + self.objet.name + "\n\nAucun objet porte le nom que vous avez saisi."
            return msg.about(w, titre, texte)
        
        maDuree = self.getData("Duree deplacement")
        if(maDuree <= 0):
            w = MainWindow()
            msg = QMessageBox()
            titre = "Erreur"
            texte = "Erreur au node " + self.name + ": \nPin : " + self.duree.name + "\n\nUne durée ce doit d'être strictement positive."
            return msg.about(w, titre, texte)          
        
        monPointDeDepart = self.getData("Point de depart")
        monPointDeFin = self.getData("Point de fin")
        monEstBoucle = self.getData("Boucle")
        monEstAllerRetour = self.getData("Aller-retour")

        translation = TranslationRectiligneSansCourbe(self, monObjet, monPointDeDepart, monPointDeFin, maDuree, monEstBoucle, monEstAllerRetour)
        translation.translater()

        self.setData("Position finale", monPointDeFin)

    @staticmethod
    def category():
        return 'Translation'

    @staticmethod
    def description():
        return "Fait bouger des bails"
    
class MainWindow(QMainWindow):
    def init(self):
        QMainWindow.init(self)