from PySide import QtCore, QtGui
import FreeCAD
import FreeCADGui

import sys
import PySide2
from PyFlow.App import PyFlow
from Qt.QtWidgets import QApplication
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow

import os 

import sys
from PyFlow import graphUiParser


app = PySide2.QtWidgets.QApplication

__dir__ = os.path.dirname(__file__)

# FreeCAD Command made with a Python script
def OpenPyFlowCmd():
    
    #app = QApplication(sys.argv)
    print("test")

    instance = PyFlow.instance(software="standalone")

    if instance is not None:

        app.setActiveWindow(instance)
        instance.show()
        # Bug Problème avec le sys.exit() peut etre parce que demande de confirmation à la fermeture de FreeCAD
"""
        try:
            sys.exit(app.exec_())

        except Exception as e:
            print(e)
"""  

# GUI command that links the Python script
class _OpenPyFlowCmd:
    """Command to create a box"""
    
    def Activated(self):
        # what is done when the command is clicked
        print("démarrage")
        OpenPyFlowCmd()

    def GetResources(self):
        # icon and command information
        MenuText = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Box')
        ToolTip = QtCore.QT_TRANSLATE_NOOP(
            'Basic1_Box',
            'Creates a new box')
        return {
            'Pixmap': __dir__ + '/icons/basic1_makebox_cmd.svg',
            'MenuText': MenuText,
            'ToolTip': ToolTip}

    def IsActive(self):
        # The command will be active if there is an active document
        return not FreeCAD.ActiveDocument is None

FreeCADGui.addCommand('OpenPyFlowCmd', _OpenPyFlowCmd())