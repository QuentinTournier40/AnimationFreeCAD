from nine import str
from PyFlow.UI.Tool.Tool import ShelfTool
from PyFlow.Core.Common import Direction
from PyFlow.Packages.Dalmau.Class.NodeCourant import NodeCourant
from Qt import QtGui


class ContinuerMouvements(ShelfTool):
    """docstring for StopperMouvements."""
    def __init__(self):
        super(ContinuerMouvements, self).__init__()

    @staticmethod
    def toolTip():
        return "Continuer tous les mouvements en cours"

    @staticmethod
    def getIcon():
        return QtGui.QIcon(":brick.png")

    @staticmethod
    def name():
        return str("ContinuerMouvements")

    def do(self):
        print("Est ce que ça marche ?")
        NodeCourant.getInstance().continuerNodesCourant()
