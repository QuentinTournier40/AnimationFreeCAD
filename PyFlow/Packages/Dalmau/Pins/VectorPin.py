from PyFlow.Core import PinBase
from PyFlow.Core.Common import *
from FreeCAD import Vector

import json

class VectorEncoder(json.JSONEncoder):
    def default(self, vecteur):
        if isinstance(vecteur, Vector):
            return {Vector.__name__: [vecteur.x,vecteur.y,vecteur.z]}
        json.JSONEncoder.default(self, vecteur)

class VectorDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(VectorDecoder, self).__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, vecteurDict):
        return Vector(vecteurDict[Vector.__name__])

def setDataG(self,data):
    super(self.__class__, self).setData(data)
    try:
        if  self.direction == PinDirection.Input and not self.hasConnections():
            self.owningNode().compute()
    except:
        pass

class VectorPin(PinBase):
    def __init__(self, name, parent, direction, **kwargs):
        super(VectorPin, self).__init__(name, parent, direction, **kwargs)

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def supportedDataTypes():
        return ('VectorPin')

    @staticmethod
    def color():
        return (200, 200, 50, 255)

    @staticmethod
    def pinDataTypeHint():
        return 'VectorPin', Vector()

    @staticmethod
    def jsonEncoderClass():
        return VectorEncoder

    @staticmethod
    def jsonDecoderClass():
        return VectorDecoder

    @staticmethod
    def internalDataStructure():
        return Vector

    @staticmethod
    def processData(data):
        return VectorPin.internalDataStructure()(data)

    def setData(self, data):
        setDataG(self, data)

