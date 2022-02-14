from abc import ABC, abstractmethod
from Qt.QtWidgets import *
from PySide import QtCore
import FreeCAD

RAFRAICHISSEMENT = 20
NOMBRE_D_OR = 32

class Mouvement(ABC):
    def __init__(self, unNode):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(RAFRAICHISSEMENT)
        self.etape = 0
        self.estBoucleAller = False

        self.sortieNode = unNode.sortieNode
        self.objet = FreeCAD.ActiveDocument.getObjectsByLabel(unNode.objet.getData())[0]
        self.estBoucle = unNode.estBoucle.getData()
        self.estAllerRetour = unNode.estAllerRetour.getData()
        self.duree = unNode.duree.getData()

class FenetreErreur():
    def __init__(self, titre, nomNode, nomPin, erreur):
        fenetre = MainWindow()
        msg = QMessageBox()
        texte = "Erreur au node : " + nomNode + "\nPin : " + nomPin + "\n\n" + erreur
        return msg.about(fenetre, titre, texte)

class MainWindow(QMainWindow):
    def init(self):
        QMainWindow.init(self)


        

"""
    @abstractmethod
    def repetitionMouvement(self):
        pass

    @abstractmethod
    def repetitionMouvementSansFin(self):
        pass

    @abstractmethod
    def repetitionMouvementAllerRetour(self):
        pass

    @abstractmethod
    def repetitionMouvementSansFinEtAllerRetour(self):
        pass

    @abstractmethod
    def allerEtapeX(self,etape):
        pass

    @abstractmethod
    def lancerMouvement(self):
        pass

    @abstractmethod
    def allerEtapePrecedante(self):
        pass

    @abstractmethod
    def allerEtapeSuivante(self):
        pass"""

    
    