from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from FreeCAD import Vector

class CreateVecteurNode(NodeBase):
    def __init__(self, name):
        super(CreateVecteurNode, self).__init__(name)
        self.createInputPin("x", "FloatPin")
        self.createInputPin("y", "FloatPin")
        self.createInputPin("z", "FloatPin")
        self.createOutputPin("Vecteur", "VectorPin")
        
    def compute(self, *args, **kwargs):
        x = self.getData("x")
        y = self.getData("y")
        z = self.getData("z")
        self.setData("Vecteur", Vector(x,y,z))

    @staticmethod
    def category():
        return 'fr|Vecteur'

    @staticmethod
    def description():
        return "Construit un vecteur a partir de ses 3 composantes."