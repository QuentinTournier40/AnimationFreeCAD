from PyFlow.Core import PinBase
from PyFlow.Core.Common import *
import FreeCAD

class FakeTypeVTFJO(object):
    """docstring for FakeTypeVTFJO"""
    def __init__(self, value=None):
        super(FakeTypeVTFJO, self).__init__()
        self.value = value

class VectorPin(PinBase):
    def __init__(self, name, owningNode, direction):
        super().__init__(name, owningNode, direction)
        self.setDefaultValue(FreeCAD.Vector(0,0,0))
    
    @staticmethod
    def IsValuePin():
        return True
    
    @staticmethod
    def supportedDataTypes():
        return ('IntPin', 'FloatPin',)
    
    @staticmethod
    def color():
        return (65, 0, 255, 255)

    @staticmethod
    def pinDataTypeHint():
        return 'IntPin', 'FloatPin', ''

    @staticmethod
    def internalDataStructure():
        return FakeTypeVTFJO

    @staticmethod
    def processData(data):
        return DemoPin.internalDataStructure()(data)