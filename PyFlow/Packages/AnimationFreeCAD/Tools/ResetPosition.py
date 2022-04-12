from PyFlow.Packages.AnimationFreeCAD.Class.Coordonnees import Coordonnees
from nine import str
from PyFlow.UI.Tool.Tool import ShelfTool
from PyFlow.Packages.AnimationFreeCAD.Class.MouvementEnCours import MouvementEnCours
from PySide2 import QtGui

import os
scriptDir = os.path.dirname(os.path.realpath(__file__))

class ResetPosition(ShelfTool):
    """docstring for ResetPosition."""
    def __init__(self):
        super(ResetPosition, self).__init__()

    @staticmethod
    def toolTip():
        return "Réinitialisation des positions des objets"

    @staticmethod
    def getIcon():
        path = "../../../../icons/boutonReset.svg"
        return QtGui.QIcon(scriptDir + os.path.sep + path)

    @staticmethod
    def name():
        return str("ResetPosition")

    def do(self):
        print("Est ce que ça marche ?")
        Coordonnees.getInstance().positionnerDebut()
