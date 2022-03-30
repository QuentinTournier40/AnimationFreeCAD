from PyFlow.Packages.AnimationFreeCAD.Class.Rotation import Rotation
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.NodeAnimation import NodeAnimation
from PyFlow.Packages.AnimationFreeCAD.Class.Animation import Animation
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from FreeCAD import Vector

import FreeCAD

class SpinAroundBySpeedNode(NodeAnimation):
    def __init__(self, name):
        super(SpinAroundBySpeedNode, self).__init__(name)
        self.createInputPin("Rotation axis", "VectorPin", Vector(0,0,1))
        self.centreRotation = Vector(0,0,0)
        self.createInputPin("Angle at start of rotation", "FloatPin")
        self.createInputPin("Angle at end of rotation", "FloatPin")
        self.createOutputPin("End angle", "FloatPin")
        self.vitesse = self.createInputPin("Speed", "FloatPin")

    def compute(self, *args, **kwargs):
        if(self.getData("Object") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Error", self.name, self.objet.name, "Please choose an object.")  
        if(self.getData("Speed") <= 0):
            return FenetreErreur("Error", self.name, self.vitesse.name, "Speed cannot be less than or equal to 0.")

        objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Object"))[0]
        axeDeRotation = self.getData("Rotation axis")               
        angleDeDebut = self.getData("Angle at start of rotation")        
        angleDeFin = self.getData("Angle at end of rotation")  
        vitesse = self.getData("Speed")

        super().compute()        

        self.mouvement = Rotation(axeDeRotation, self.centreRotation, angleDeDebut, angleDeFin,self)
        self.animation.executionVitesse(self.mouvement,objet, vitesse)   

        self.setData("Final position", objet.Placement.Base)
        self.setData("End angle", angleDeFin)
        self.setData("Object use", objet.Label)

    @staticmethod
    def category():
        return 'en|Spin|Speed'

    @staticmethod
    def description():
        return "Rotates objects on itself"