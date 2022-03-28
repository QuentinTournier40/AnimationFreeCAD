from nine import str
from PyFlow.UI.Tool.Tool import ShelfTool
from PyFlow.Core.Common import Direction
from PyFlow.Packages.AnimationFreeCAD.Class.NodeCourant import NodeCourant
from Qt import QtGui

import os 
scriptDir = os.path.dirname(os.path.realpath(__file__))

class MettreEnPause(ShelfTool):
    """docstring for StopperMouvements."""
    def __init__(self):
        super(MettreEnPause, self).__init__()

    @staticmethod
    def toolTip():
        return "Mets en pause tous les mouvements en cours"

    @staticmethod
    def getIcon():
        path = "../../../../icons/boutonPause.svg"
        return QtGui.QIcon(scriptDir + os.path.sep + path)

    @staticmethod
    def name():
        return str("Mettre en pause")

    def do(self):
        print("Est ce que ça marche ?")
        NodeCourant.getInstance().stopperNodesCourant()
