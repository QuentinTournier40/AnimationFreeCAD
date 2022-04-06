from PySide import QtCore
from PyFlow.App import PyFlow
from PyFlow.Packages.AnimationFreeCAD.Class.Coordonnees import Coordonnees

import FreeCAD
import FreeCADGui
import PySide2
import os 

app = PySide2.QtWidgets.QApplication

__dir__ = os.path.dirname(__file__)

global instancePyFlow
instancePyFlow = PyFlow()

# FreeCAD Command made with a Python script
def OpenPyFlowCmd():
    
    if(instancePyFlow.appInstance == None):
        instancePyFlow.instance(software="standalone")        
        app.setActiveWindow(instancePyFlow.appInstance)
        instancePyFlow.appInstance.show()
        Coordonnees.getInstance().ajouterEtape()
    else:
        app.setActiveWindow(instancePyFlow.appInstance)

# GUI command that links the Python script
class _OpenPyFlowCmd:
    """Command to create a box"""
    
    def Activated(self):
        # what is done when the command is clickede
        OpenPyFlowCmd()

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'premierIcone',
            'Box')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'premierIcone',
            'Open PyFlow')
        return {
            'Pixmap': __dir__ + '/icons/openPyFlow.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

FreeCADGui.addCommand('OpenPyFlowCmd', _OpenPyFlowCmd())