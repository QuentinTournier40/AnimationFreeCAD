from abc import ABC
from Qt.QtWidgets import *

import time

RAFRAICHISSEMENT = 20
NOMBRE_D_OR = 32
DEFAULT_VALUE_OBJECT_PIN = "---Select object---"

class Mouvement(ABC):
    def __init__(self, unNode):
        self.timer = None
        self.etape = 0
        self.node = unNode
        self.objet = None

    def stopperMouvement(self):
        if(self.timer.isActive()):
            self.timer.stop()
    
    def activerMouvement(self):
        if(not self.timer.isActive()):
            self.timer.start()
    
    def getEtape(self):
        return self.etape

    def getEtapeMax(self):
        return self.nbrPoints

    def setObjet(self, objet):
        self.objet = objet

    def executionAller(self, sortie):
        self.execution(True,sortie)
        self.monTemps = time.time()
    
    def executionAllerRetour(self, sortie):
        self.execution(True,"self.execution(False, \""+ sortie + "\")")
        self.monTemps = time.time()

    def executionAllerBoucle(self):
        self.execution(True, "self.executionAllerBoucle()")
        self.monTemps = time.time()

    def executionBoucleAllerRetour(self):
        self.executionAllerRetour("self.executionBoucleAllerRetour()")
        self.monTemps = time.time()

    def memeMouvement(self,unMouvement):
        resultat = False
        if(self.objet == unMouvement.objet):
            resultat = True
        return resultat

class FenetreErreur():
    def __init__(self, titre, nomNode, nomPin, erreur):
        fenetre = MainWindow()
        msg = QMessageBox()
        texte = "Erreur au node : " + nomNode + "\nPin : " + nomPin + "\n\n" + erreur
        return msg.about(fenetre, titre, texte)

class MainWindow(QMainWindow):
    def init(self):
        QMainWindow.init(self)