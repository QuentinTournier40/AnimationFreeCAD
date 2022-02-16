from re import X
from threading import local
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

global instancePyFlow
instancePyFlow = PyFlow()

def OpenPyFlowCmd():

    global instancePyFlow
    if(instancePyFlow.appInstance == None):
        instancePyFlow.instance(software="standalone")        
        app.setActiveWindow(instancePyFlow.appInstance)
        instancePyFlow.appInstance.show()
        print("dedans")
    else:
        print("dehors")
        app.setActiveWindow(instancePyFlow.appInstance)

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