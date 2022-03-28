from PyFlow.Core.Common import *
from PyFlow.Core import FunctionLibraryBase
from PyFlow.Core import IMPLEMENT_NODE
from FreeCAD import Vector


class VectorLib(FunctionLibraryBase):
    '''doc string for VectorLib'''

    def __init__(self, packageName):
        super(VectorLib, self).__init__(packageName)
    
    @staticmethod
    @IMPLEMENT_NODE(returns=('VectorPin', Vector()), meta={NodeMeta.CATEGORY: 'Vector', NodeMeta.KEYWORDS: []})
    def makeVector(vecteur=('VectorPin', Vector())):
        """make a Vector"""
        return vecteur
    
    @staticmethod
    @IMPLEMENT_NODE(returns=('VectorPin', Vector()), meta={NodeMeta.CATEGORY: 'Vector', NodeMeta.KEYWORDS: []})
    def createVector(x=('FloatPin', 0.0), y=('FloatPin', 0.0), z=('FloatPin', 0.0)):
        """Create a Vector"""
        return Vector(x,y,z)