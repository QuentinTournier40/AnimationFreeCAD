from PyFlow.Packages.Dalmau.Class.Rotation import Rotation
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from FreeCAD import Vector
from Qt.QtWidgets import *

import FreeCAD

class RotationNode(NodeAnimation):
    
    def __init__(self, name):
        super(RotationNode, self).__init__(name)
        self.axeRotation = self.createInputPin("Axe de rotation", "VectorPin", Vector(0,0,1))
        self.centreRotation = self.createInputPin("Centre de rotation", "VectorPin")
        self.angleDebut = self.createInputPin("Angle au debut de la rotation", "FloatPin")
        self.angleFin = self.createInputPin("Angle a la fin de la rotation", "FloatPin")
        self.angleFinal = self.createOutputPin("Angle final", "FloatPin")
        self.duree = self.createInputPin("Duree", "FloatPin")

    def compute(self, *args, **kwargs):
        try:
            FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        except IndexError:
            w = MainWindow()
            msg = QMessageBox()
            titre = "Erreur"
            texte = "Erreur au node " + self.name + ": \nPin : " + self.objet.name + "\n\nAucun objet porte le nom que vous avez saisi."
            return msg.about(w, titre, texte)
        
        if(self.duree.getData() <= 0):
            w = MainWindow()
            msg = QMessageBox()
            titre = "Erreur"
            texte = "Erreur au node " + self.name + ": \nPin : " + self.duree.name + "\n\nUne durée ce doit d'être strictement positive."
            return msg.about(w, titre, texte)

        
        rotation = Rotation(self)
        rotation.rotation()

        #self.setData("Position finale", self.monObjet.Placement.Base)
        #self.setData("Angle final", monAngleFin)

    @staticmethod
    def category():
        return 'Rotation'

    @staticmethod
    def description():
        return "Fait tourner des bails"

class MainWindow(QMainWindow):
    def init(self):
        QMainWindow.init(self)