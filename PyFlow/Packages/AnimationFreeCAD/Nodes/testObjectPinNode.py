from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *


class testObjectPinNode(NodeBase):
    def __init__(self, name):
        super(testObjectPinNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createOutputPin("outExec", "ExecPin")
        self.createInputPin("Object", "ObjectPin", "---Select object---")
        self.createOutputPin("Object", "ObjectPin", "---Select object---")
        self.createInputPin("Curve", "CurvePin", "---Select object---")
        self.createOutputPin("Curve", "CurvePin", "---Select object---")

    def execute(self, *args, **kwargs):
        truc = self.getData("Object")
        truc2 = self.getData("Curve")
        #print(truc)
        #print(truc2)
        self["outExec"].call()

    @staticmethod
    def category():
        return 'Autre'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return "Lance plusieurs node en meme temps"
