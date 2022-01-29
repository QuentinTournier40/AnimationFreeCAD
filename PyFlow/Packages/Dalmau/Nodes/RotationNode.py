from PyFlow.Packages.Dalmau.Class.Rotation import Rotation
from PyFlow.Packages.Dalmau.Class.NodeAnimation import NodeAnimation
import FreeCAD

class RotationNode(NodeAnimation):
    
    def __init__(self, name):
        super(RotationNode, self).__init__(name)
        self.createInputPin("X axe de rotation", "FloatPin")
        self.createInputPin("Y axe de rotation", "FloatPin")
        self.createInputPin("Z axe de rotation", "FloatPin")
        self.createInputPin("X centre de rotation", "FloatPin")
        self.createInputPin("Y centre de rotation", "FloatPin")
        self.createInputPin("Z centre de rotation", "FloatPin")
        self.createInputPin("Angle au debut de la rotation", "FloatPin")
        self.createInputPin("Angle a la fin de la rotation", "FloatPin")

    def compute(self, *args, **kwargs):
        monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        monAxeDeRotation = FreeCAD.Vector(self.getData("X axe de rotation"), self.getData("Y axe de rotation"), self.getData("Z axe de rotation"))
        monCentreDeRotation = FreeCAD.Vector(self.getData("X centre de rotation"), self.getData("Y centre de rotation"), self.getData("Z centre de rotation"))
        monAngleDebut = self.getData("Angle au debut de la rotation")
        monAngleFin = self.getData("Angle a la fin de la rotation")
        maDuree = self.getData("Duree deplacement")
        monEstBoucle = self.getData("Realiser en boucle ?")
        monEstAllerRetour = self.getData("Realiser en aller-retour")
        
        rotation = Rotation(self, monObjet, monAxeDeRotation, monCentreDeRotation, monAngleDebut, monAngleFin, maDuree, monEstBoucle, monEstAllerRetour)
        rotation.rotation()

    @staticmethod
    def category():
        return 'Rotation'

    @staticmethod
    def description():
        return "Fait tourner des bails"