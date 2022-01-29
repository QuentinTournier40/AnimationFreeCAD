from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *


class getValueVector(NodeBase):
    def __init__(self, name):
        super(getValueVector, self).__init__(name)
        self.createInputPin("Vecteur", "VectorPin")
        self.createOutputPin("X", "FloatPin")
        self.createOutputPin("Y", "FloatPin")
        self.createOutputPin("Z", "FloatPin")
        
    def compute(self, *args, **kwargs):
        vecteur = self.getData("Vecteur")
        self.setData("x", vecteur.x)
        self.setData("y", vecteur.y)
        self.setData("z", vecteur.z)

    @staticmethod
    def category():
        return 'Vector'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "..."
