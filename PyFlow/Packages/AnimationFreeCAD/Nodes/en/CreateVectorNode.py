from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from FreeCAD import Vector

class CreateVectorNode(NodeBase):
    def __init__(self, name):
        super(CreateVectorNode, self).__init__(name)
        self.createInputPin("x", "FloatPin")
        self.createInputPin("y", "FloatPin")
        self.createInputPin("z", "FloatPin")
        self.createOutputPin("Vector", "VectorPin")
        
    def compute(self, *args, **kwargs):
        x = self.getData("x")
        y = self.getData("y")
        z = self.getData("z")
        self.setData("Vector", Vector(x,y,z))

    @staticmethod
    def category():
        return 'en|Vector'

    @staticmethod
    def description():
        return "Build a vector with its 3 components."