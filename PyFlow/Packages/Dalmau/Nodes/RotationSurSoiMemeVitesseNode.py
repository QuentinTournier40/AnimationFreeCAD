from PyFlow.Packages.Dalmau.Class.Rotation import Rotation
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from PyFlow.Packages.Dalmau.Class.Animation import Animation
from PyFlow.Packages.Dalmau.Class.Mouvement import FenetreErreur
from FreeCAD import Vector
from Qt.QtWidgets import *

import FreeCAD

class RotationSurSoiMemeVitesseNode(NodeAnimation):
    def __init__(self, name):
        super(RotationSurSoiMemeVitesseNode, self).__init__(name)
        self.axeRotation = self.createInputPin("Axe de rotation", "VectorPin", Vector(0,0,1))
        self.centreRotation = Vector(0,0,0)
        self.angleDebut = self.createInputPin("Angle au debut de la rotation", "FloatPin")
        self.angleFin = self.createInputPin("Angle a la fin de la rotation", "FloatPin")
        self.angleFinal = self.createOutputPin("Angle final", "FloatPin")
        self.vitesse = self.createInputPin("Vitesse", "FloatPin")

    def compute(self, *args, **kwargs):
        try:
            objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        except IndexError:
            return FenetreErreur("Erreur", self.name, self.objet.name, "Aucun objet ne porte le nom que vous avez saisi.")    
        
        if(self.vitesse.getData() <= 0):
            return FenetreErreur("Erreur", self.name, self.vitesse.name, "La vitesse ne peut pas être inférieure ou égale à 0.") 

        axeDeRotation = self.axeRotation.getData()               
        angleDeDebut = self.angleDebut.getData()        
        angleDeFin = self.angleFin.getData()  

        vitesse = self.vitesse.getData()        
        estBoucle = self.estBoucle.getData()        
        estAllerRetour = self.estAllerRetour.getData()        

        rotation = Rotation(axeDeRotation, self.centreRotation, angleDeDebut, angleDeFin,self)
        animation = Animation(estBoucle, estAllerRetour, self)
        animation.executionVitesse(rotation,objet,vitesse)   

        #self.setData("Position finale", monObjet.Placement.Base)
        #self.setData("Angle final", monAngleFin)

    @staticmethod
    def category():
        return 'Rotation|Vitesse'

    @staticmethod
    def description():
        return "Fait tourner des bails"