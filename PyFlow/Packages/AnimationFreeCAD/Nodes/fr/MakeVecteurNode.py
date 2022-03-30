from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *

class MakeVecteurNode(NodeBase):
    def __init__(self, name):
        super(MakeVecteurNode, self).__init__(name)
        self.createInputPin("Vecteur", "VectorPin")
        self.createOutputPin("Vecteur sortie", "VectorPin")
        
    def compute(self, *args, **kwargs):
        vecteur = self.getData("Vecteur")
        self.setData("Vecteur sortie", vecteur)

    @staticmethod
    def category():
        return 'fr|Vecteur'

    @staticmethod
    def description():
        return "Retourn le vecteur de l'input."