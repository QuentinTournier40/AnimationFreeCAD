import functools
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PySide import QtCore
import FreeCAD


class WaitNode(NodeBase):
    def __init__(self, name):
        super(WaitNode, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createOutputPin("outExec", "ExecPin")

        self.createInputPin("Waiting time", "FloatPin")


    def execute(self, *args, **kwargs):
        self.tempsAttente = self.getData("Waiting time")
        self.compteur = 0

        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)

        mouvement = functools.partial(self.attendre)

        self.timer.timeout.connect(mouvement)
        self.timer.start()

    def attendre(self):
        if(self.compteur >= self.tempsAttente):
            self.timer.stop()
            self["outExec"].call()
        else:
            self.compteur += 0.032

    @staticmethod
    def category():
        return 'en|Other'

    @staticmethod
    def description():
        return "Wait for the given time"
