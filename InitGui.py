import os
import FreeCAD as App
import FreeCADGui as Gui

class AnimationFreeCAD(Workbench):
    def __init__(self):
        path = os.getcwd()

        self.__class__.MenuText = "AnimationFreeCAD"
        self.__class__.ToolTip = "Faire des animations"
        self.__class__.Icon = os.path.join(App.getResourceDir(),"../"
                                           "Mod", "AnimationFreeCAD",
                                           "icons",
                                           "clapCinema.svg")

    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        import pyflow_start
        from PySide import QtCore, QtGui
        import PyFlow # import here all the needed files that create your FreeCAD commands

        self.list = ["OpenPyFlowCmd"] # A list of command names created in the line above
        self.appendToolbar("open", self.list)

Gui.addWorkbench(AnimationFreeCAD())
