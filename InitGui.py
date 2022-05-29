import os
import FreeCAD as App
import FreeCADGui as Gui

from pivy import coin


class AnimationFreeCAD(Workbench):
    def __init__(self):
        self.__class__.MenuText = "AnimationFreeCAD"
        self.__class__.ToolTip = "Faire des animations"
        self.__class__.Icon = os.path.join(App.getUserAppDataDir(),
                                           "Mod", "AnimationFreeCAD",
                                           "icons",
                                           "clapCinema.svg")

    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        from PyFlow.App import PyFlow
        self.instance = PyFlow.instance(None, "freecad")

    def Activated(self):
        """This function is executed when the workbench is activated"""
        from PySide2 import QtWidgets
        mw = Gui.getMainWindow()
        mdiArea = mw.findChild(QtWidgets.QMdiArea)
        mdiArea.addSubWindow(self.instance)
        self.instance.show()

    def Deactivated(self):
        """This function is executed when the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This function is executed whenever the user right-clicks on screen"""
        pass

    def GetClassName(self):
        """ This function is mandatory if this is a full Python workbench"""
        return "Gui::PythonWorkbench"

Gui.addWorkbench(AnimationFreeCAD())
