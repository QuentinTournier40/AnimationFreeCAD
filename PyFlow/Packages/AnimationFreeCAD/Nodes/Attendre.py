from dis import dis
import functools
from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PySide import QtCore
import FreeCAD


class Attendre(NodeBase):
    def __init__(self, name):
        super(Attendre, self).__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createOutputPin("outExec", "ExecPin")

        self.createInputPin("Temps d'attente", "FloatPin")


    def execute(self, *args, **kwargs):
        self.tempsAttente = self.getData("Temps d'attente")
        self.compteur = 0

        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)

        mouvement = functools.partial(self.truc)

        self.timer.timeout.connect(mouvement)
        self.timer.start()

    def truc(self):
        if(self.compteur >= self.tempsAttente):
            self.timer.stop()
            self["outExec"].call()
        else:
            self.compteur += 0.032

    @staticmethod
    def category():
        return 'Autre'

    @staticmethod
    def description():
        return "Lance plusieurs node en meme temps"
