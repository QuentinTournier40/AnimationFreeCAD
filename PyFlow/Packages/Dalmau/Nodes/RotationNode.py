from PyFlow.Packages.Dalmau.Class.AnimationParam import AnimationParam
from PyFlow.Packages.Dalmau.Class.RotationParam import RotationParam
from PyFlow.Packages.Dalmau.Class.Rotation import Rotation
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from PyFlow.Packages.Dalmau.Class.Mouvement import FenetreErreur
from FreeCAD import Vector
from PyFlow.Packages.Dalmau.Class.rotationParam import RotationParam
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
            return FenetreErreur("Erreur", self.name, self.objet.name, "Aucun objet ne porte le nom que vous avez saisi.")    
        
        axeDeRotation = self.axeRotation.getData()        
        centreDeRotation = self.centreRotation.getData()        
        angleDeDebut = self.angleDebut.getData()        
        angleDeFin = self.angleFin.getData()  

        duree = self.duree.getData()        
        estBoucle = self.estBoucle.getData()        
        estAllerRetour = self.estAllerRetour.getData()        
        nomNode = self.name

        parametreRotation = RotationParam(axeDeRotation, centreDeRotation, angleDeDebut, angleDeFin)
        parametreAnimation = AnimationParam()

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