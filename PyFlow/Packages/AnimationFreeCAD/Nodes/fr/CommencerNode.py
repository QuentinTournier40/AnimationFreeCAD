from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *

class CommencerNode(NodeBase):
    def __init__(self, name):
        super(CommencerNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createOutputPin("outExec", "ExecPin")

    def execute(self, *args, **kwargs):
        self["outExec"].call()

    @staticmethod
    def category():
        return 'fr|Autre'

    @staticmethod
    def description():
        return "Lance plusieurs node en meme temps."