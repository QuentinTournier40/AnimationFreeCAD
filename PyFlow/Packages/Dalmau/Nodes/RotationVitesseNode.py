from PyFlow.Packages.Dalmau.Class.Rotation import Rotation
from PyFlow.Packages.Dalmau.Class.Animation import Animation
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
from PyFlow.Packages.Dalmau.Class.Mouvement import *
from FreeCAD import Vector

import FreeCAD

class RotationVitesseNode(NodeAnimation):
    def __init__(self, name):
        super(RotationVitesseNode, self).__init__(name)
        self.createInputPin("Axe de rotation", "VectorPin", Vector(0,0,1))
        self.createInputPin("Centre de rotation", "VectorPin")
        self.createInputPin("Angle au debut de la rotation", "FloatPin")
        self.createInputPin("Angle a la fin de la rotation", "FloatPin")
        self.createOutputPin("Angle final", "FloatPin")
        self.vitesse = self.createInputPin("Vitesse", "FloatPin")

    def compute(self, *args, **kwargs):
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")  
        if(self.getData("Vitesse") <= 0):
            return FenetreErreur("Erreur", self.name, self.vitesse.name, "La vitesse ne peut pas être inférieure ou égale à 0.")

        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        axeDeRotation = self.getData("Axe de rotation")        
        centreDeRotation = self.getData("Centre de rotation")        
        angleDeDebut = self.getData("Angle au debut de la rotation")        
        angleDeFin = self.getData("Angle a la fin de la rotation")  
        vitesse = self.getData("Vitesse")

        super().compute()        

        self.mouvement = Rotation(axeDeRotation, centreDeRotation, angleDeDebut, angleDeFin,self)
        self.animation.executionVitesse(self.mouvement,objet, vitesse)

        self.setData("Position finale", objet.Placement.Base)
        self.setData("Angle final", angleDeFin)
        self.setData("Objet use", objet.Label)

    @staticmethod
    def category():
        return 'Rotation|Vitesse'

    @staticmethod
    def description():
        return "Fait tourner des objets."