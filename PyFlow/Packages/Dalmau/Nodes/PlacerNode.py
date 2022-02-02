from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from Qt.QtWidgets import *

import FreeCAD


class PlacerNode(NodeBase):
    def __init__(self, name):
        super(PlacerNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.objet = self.createInputPin("Objet","StringPin")
        self.coordonnees = self.createInputPin("Coordonnees","VectorPin")
        self.createOutputPin("outExec", "ExecPin")
        self.createOutputPin("Coordonnees de fin","VectorPin")

    def execute(self, *args, **kwargs):
        try:
            monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        except IndexError:
            w = MainWindow()
            msg = QMessageBox()
            titre = "Erreur"
            texte = "Erreur au node " + self.name + ": \nPin : " + self.objet.name + "\n\nAucun objet porte le nom que vous avez saisi."
            return msg.about(w, titre, texte)
        
        monObjet.Placement.Base = self.getData("Coordonnees")
        self.setData("Coordonnees de fin", self.getData("Coordonnees"))
        self["outExec"].call()

    @staticmethod
    def category():
        return 'Autre'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Place un objet aux coordonées données"

class MainWindow(QMainWindow):
    def init(self):
        QMainWindow.init(self)