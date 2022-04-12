from PySide2.QtWidgets import *


class FenetreErreur():
    def __init__(self, titre, nomNode, nomPin, erreur):
        fenetre = MainWindow()
        msg = QMessageBox()
        texte = "Node : " + nomNode + "\nPin : " + nomPin + "\n\n" + erreur
        return msg.about(fenetre, titre, texte)

class MainWindow(QMainWindow):
    def init(self):
        QMainWindow.init(self)
