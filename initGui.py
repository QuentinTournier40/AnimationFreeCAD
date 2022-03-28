import os

class AnimationFreeCAD(Workbench):
    path = os.getcwd()

    MenuText = "AnimationFreeCAD"
    ToolTip = "Faire des animations"
    Icon = path + "/../Mod/AnimationFreeCAD/icons/clapCinema.svg"

    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        import testFunc
        from PySide import QtCore, QtGui
        import PyFlow # import here all the needed files that create your FreeCAD commands

        self.list = ["OpenPyFlowCmd"] # A list of command names created in the line above
        self.appendToolbar(str(QtCore.QT_TRANSLATE_NOOP("basic1", "basic1")), self.list)

Gui.addWorkbench(AnimationFreeCAD())