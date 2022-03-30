from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *

class MakeVectorNode(NodeBase):
    def __init__(self, name):
        super(MakeVectorNode, self).__init__(name)
        self.createInputPin("Vector", "VectorPin")
        self.createOutputPin("Output vector", "VectorPin")
        
    def compute(self, *args, **kwargs):
        vecteur = self.getData("Vector")
        self.setData("Output vector", vecteur)
        
    @staticmethod
    def category():
        return 'en|Vector'

    @staticmethod
    def description():
        return "Return the input vector"