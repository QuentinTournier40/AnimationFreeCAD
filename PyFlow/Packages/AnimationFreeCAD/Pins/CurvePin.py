from PyFlow.Core import PinBase
from PyFlow.Packages.AnimationFreeCAD.Pins.ObjectPin import ObjetDecoder, ObjetEncoder

class CurvePin(PinBase):
    def __init__(self, name, parent, direction, **kwargs):
        super(CurvePin, self).__init__(name, parent, direction,)
        self.setDefaultValue(None)

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def supportedDataTypes():
        return ('CurvePin',)

    @staticmethod
    def color():
        return (150, 150, 250, 255)

    @staticmethod
    def pinDataTypeHint():
        return 'CurvePin'

    @staticmethod
    def jsonEncoderClass():
        return ObjetEncoder

    @staticmethod
    def jsonDecoderClass():
        return ObjetDecoder

    @staticmethod
    def internalDataStructure():
        return String

    @staticmethod
    def processData(data):
        return data

class String():
    def __init__(self):
        pass