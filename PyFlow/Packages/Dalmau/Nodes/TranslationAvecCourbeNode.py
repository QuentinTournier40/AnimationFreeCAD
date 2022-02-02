from fnmatch import translate
from PyFlow.Packages.Dalmau.Class.TranslationAvecCourbe import TranslationAvecCourbe
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from Qt.QtWidgets import *

import FreeCAD

class TranslationAvecCourbeNode(NodeAnimation):
    
    def __init__(self, name):
        super(TranslationAvecCourbeNode, self).__init__(name)
        self.createInputPin("Courbe", "StringPin")
    
    def compute(self, *args, **kwargs):
        try:
            monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        except IndexError:
            w = MainWindow()
            msg = QMessageBox()
            titre = "Erreur"
            texte = "Erreur au node " + self.name + ": \nPin : " + self.objet.name + "\n\nAucun objet porte le nom que vous avez saisi."
            return msg.about(w, titre, texte)
        
        try:
            maCourbe = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Courbe"))[0]
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

        monEstBoucle = self.getData("Boucle")
        monEstAllerRetour = self.getData("Aller-retour")

        translation = TranslationAvecCourbe(self, monObjet, maDuree, monEstBoucle, monEstAllerRetour, maCourbe)
        translation.translater()

    @staticmethod
    def category():
        return 'Translation'

    @staticmethod
    def description():
        return "Fait bouger des bails en suivant la trajectoire de n'importe quel type de courbe"

class MainWindow(QMainWindow):
    def init(self):
        QMainWindow.init(self)