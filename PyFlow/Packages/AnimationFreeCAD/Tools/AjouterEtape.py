from PyFlow.Packages.AnimationFreeCAD.Class.Coordonnees import Coordonnees
from nine import str
from PyFlow.UI.Tool.Tool import ShelfTool
from PyFlow.Packages.AnimationFreeCAD.Class.NodeCourant import NodeCourant
from Qt import QtGui

import os 
scriptDir = os.path.dirname(os.path.realpath(__file__))

class AjouterEtape(ShelfTool):
    """docstring for ResetPosition."""
    def __init__(self):
        super(AjouterEtape, self).__init__()

    @staticmethod
    def toolTip():
        return "Ajoute une étape à la liste avec les paramètres de tous les objets de la fenêtre FreeCAD"

    @staticmethod
    def getIcon():
        path = "../../../../icons/boutonAjouterEtape.svg"
        return QtGui.QIcon(scriptDir + os.path.sep + path)

    @staticmethod
    def name():
        return str("AjouterEtape")

    def do(self):
        print("Est ce que ça marche ?")
        Coordonnees.getInstance().ajouterEtape()