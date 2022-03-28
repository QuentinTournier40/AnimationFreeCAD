from nine import str
from PyFlow.UI.Tool.Tool import ShelfTool
from PyFlow.Core.Common import Direction
from PyFlow.Packages.AnimationFreeCAD.Class.NodeCourant import NodeCourant
from Qt import QtGui

import os 

scriptDir = os.path.dirname(os.path.realpath(__file__))

class ContinuerMouvements(ShelfTool):
    """docstring for mettreEnPause."""
    def __init__(self):
        super(ContinuerMouvements, self).__init__()

    @staticmethod
    def toolTip():
        return "Continuer tous les mouvements en cours"

    @staticmethod
    def getIcon():
        path = "../../../../icons/boutonPlay.svg"
        return QtGui.QIcon(scriptDir + os.path.sep + path)

    @staticmethod
    def name():
        return str("ContinuerMouvements")

    def do(self):
        print("Est ce que ça marche ?")
        NodeCourant.getInstance().continuerNodesCourant()
