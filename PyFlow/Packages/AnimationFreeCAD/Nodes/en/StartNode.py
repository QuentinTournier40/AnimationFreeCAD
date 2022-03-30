from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *

class StartNode(NodeBase):
    def __init__(self, name):
        super(StartNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createOutputPin("outExec", "ExecPin")

    def execute(self, *args, **kwargs):
        self["outExec"].call()

    @staticmethod
    def category():
        return 'en|Other'

    @staticmethod
    def description():
        return "Start several nodes at the same time."