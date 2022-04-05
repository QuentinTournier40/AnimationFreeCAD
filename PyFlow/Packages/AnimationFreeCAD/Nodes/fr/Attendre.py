import functools

from PyFlow.Core import NodeBase
from PyFlow.Core.Common import *
from PySide import QtCore
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *

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

        mouvement = functools.partial(self.attendre)

        self.timer.timeout.connect(mouvement)
        self.timer.start()

    def attendre(self):
        if(self.compteur >= self.tempsAttente):
            self.timer.stop()
            self["outExec"].call()
        else:
            self.compteur += NOMBRE_D_OR / 1000

    @staticmethod
    def category():
        return 'fr|Autre'

    @staticmethod
    def description():
        return "Attends le temps donnée"
