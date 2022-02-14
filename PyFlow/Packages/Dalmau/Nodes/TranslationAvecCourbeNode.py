from PyFlow.Packages.Dalmau.Class.TranslationAvecCourbe import TranslationAvecCourbe
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from Qt.QtWidgets import *

import FreeCAD

class TranslationAvecCourbeNode(NodeAnimation):
    
    def __init__(self, name):
        super(TranslationAvecCourbeNode, self).__init__(name)
        self.courbe = self.createInputPin("Courbe", "StringPin")
        self.duree = self.createInputPin("Duree", "FloatPin")
    
    def compute(self, *args, **kwargs):
        try:
            FreeCAD.ActiveDocument.getObjectsByLabel(self.objet.getData())[0]
        except IndexError:
            w = MainWindow()
            msg = QMessageBox()
            titre = "Erreur"
            texte = "Erreur au node " + self.name + ": \nPin : " + self.objet.name + "\n\nAucun objet porte le nom que vous avez saisi."
            return msg.about(w, titre, texte)
        
        try:
            FreeCAD.ActiveDocument.getObjectsByLabel(self.courbe.getData())[0]
        except IndexError:
            w = MainWindow()
            msg = QMessageBox()
            titre = "Erreur"
            texte = "Erreur au node " + self.name + ": \nPin : " + self.courbe.name + "\n\nAucun objet porte le nom que vous avez saisi."
            return msg.about(w, titre, texte)
        
        if(self.duree.getData() <= 0):
            w = MainWindow()
            msg = QMessageBox()
            titre = "Erreur"
            texte = "Erreur au node " + self.name + ": \nPin : " + self.duree.name + "\n\nUne durée ce doit d'être strictement positive."
            return msg.about(w, titre, texte)        

        translation = TranslationAvecCourbe(self)
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