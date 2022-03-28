from nine import str
from PyFlow.UI.Tool.Tool import ShelfTool
from PyFlow.Core.Common import Direction
from PyFlow.Packages.AnimationFreeCAD.Class.NodeCourant import NodeCourant
from Qt import QtGui


class ArreterTousLesMouvements(ShelfTool):
    """docstring for ArreterTousLesMouvements."""
    def __init__(self):
        super(ArreterTousLesMouvements, self).__init__()

    @staticmethod
    def toolTip():
        return "Arrêter tous les mouvements en cours"

    @staticmethod
    def getIcon():
        return QtGui.QIcon(":brick.png")

    @staticmethod
    def name():
        return str("ArreterTousLesMouvements")

    def do(self):
        print("Est ce que ça marche ?")
        NodeCourant.getInstance().arreterLAnimation()