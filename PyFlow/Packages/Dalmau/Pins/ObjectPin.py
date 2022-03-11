import json
from PyFlow.Core import PinBase

class ObjetEncoder(json.JSONEncoder):
    def default(self, objet):
        if isinstance(objet, String):
            return {String.__name__: objet}
        json.JSONEncoder.default(self, objet)

class ObjetDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super(ObjetDecoder, self).__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, objetDict):
        return String(objetDict[String.__name__])

class ObjectPin(PinBase):
    def __init__(self, name, parent, direction, **kwargs):
        super(ObjectPin, self).__init__(name, parent, direction,)
        self.setDefaultValue(None)

    @staticmethod
    def IsValuePin():
        return True

    @staticmethod
    def supportedDataTypes():
        return ('ObjectPin',)

    @staticmethod
    def color():
        return (150, 150, 250, 255)

    @staticmethod
    def pinDataTypeHint():
        return 'ObjectPin'

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