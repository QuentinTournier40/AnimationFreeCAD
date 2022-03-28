from PyFlow.Packages.AnimationFreeCAD.Class.Coordonnees import Coordonnees
from nine import str
from PyFlow.UI.Tool.Tool import ShelfTool
from PyFlow.Packages.AnimationFreeCAD.Class.NodeCourant import NodeCourant
from Qt import QtGui

import os 
scriptDir = os.path.dirname(os.path.realpath(__file__))

class EtapePrecedente(ShelfTool):
    """docstring for ResetPosition."""
    def __init__(self):
        super(EtapePrecedente, self).__init__()

    @staticmethod
    def toolTip():
        return "Retour à l'étape précédente"

    @staticmethod
    def getIcon():
        path = "../../../../icons/boutonPrecedent.svg"
        return QtGui.QIcon(scriptDir + os.path.sep + path)

    @staticmethod
    def name():
        return str("EtapePrecedente")

    def do(self):
        print("Est ce que ça marche ?")
        Coordonnees.getInstance().etapePrecedente()