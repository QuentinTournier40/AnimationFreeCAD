from PyFlow.Packages.Dalmau.Class.Rotation import Rotation
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
import FreeCAD
from FreeCAD import Vector

class RotationNode(NodeAnimation):
    
    def __init__(self, name):
        super(RotationNode, self).__init__(name)
        self.createInputPin("Axe de rotation", "VectorPin", Vector(0,0,1))
        self.createInputPin("Centre de rotation", "VectorPin")
        self.createInputPin("Angle au debut de la rotation", "FloatPin")
        self.createInputPin("Angle a la fin de la rotation", "FloatPin")

    def execute(self, *args, **kwargs):
        monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        monAxeDeRotation = self.getData("Axe de rotation")
        monCentreDeRotation = self.getData("Centre de rotation")
        monAngleDebut = self.getData("Angle au debut de la rotation")
        monAngleFin = self.getData("Angle a la fin de la rotation")
        maDuree = self.getData("Duree deplacement")
        monEstBoucle = self.getData("Boucle")
        monEstAllerRetour = self.getData("Aller-retour")
        
        rotation = Rotation(self, monObjet, monAxeDeRotation, monCentreDeRotation, monAngleDebut, monAngleFin, maDuree, monEstBoucle, monEstAllerRetour)
        rotation.rotation()

    @staticmethod
    def category():
        return 'Rotation'

    @staticmethod
    def description():
        return "Fait tourner des bails"