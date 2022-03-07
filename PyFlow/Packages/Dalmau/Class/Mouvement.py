from abc import ABC, abstractmethod
from Qt.QtWidgets import *
from PySide import QtCore
import FreeCAD

RAFRAICHISSEMENT = 20
NOMBRE_D_OR = 32

class Mouvement(ABC):
    def __init__(self, unNode):
        self.timer = None
        #self.timer.setInterval(RAFRAICHISSEMENT)
        self.etape = 0
        self.node = unNode

    def stopperMouvement(self):
        if(self.timer.isActive()):
            self.timer.stop()
        else:
            print("He oh les timers ne sont pas actifs détends toi sale fou")
    
    def activerMouvement(self):
        if(not self.timer.isActive()):
            self.timer.start()
        else:
            print("He oh les timers sont actifs détends tu veux aller 2 fois plus vite ou quoi")
        


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

    
    