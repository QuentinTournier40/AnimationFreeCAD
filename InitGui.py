import os

class AnimationFreeCAD(Workbench):
    path = os.getcwd()

    MenuText = "AnimationFreeCAD"
    ToolTip = "Faire des animations"
    Icon = path + "/../Mod/AnimationFreeCAD/icons/clapCinema.svg"

    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        import pyflow_start
        from PySide import QtCore, QtGui
        import PyFlow # import here all the needed files that create your FreeCAD commands

        self.list = ["OpenPyFlowCmd"] # A list of command names created in the line above
        self.appendToolbar("open", self.list)

Gui.addWorkbench(AnimationFreeCAD())
