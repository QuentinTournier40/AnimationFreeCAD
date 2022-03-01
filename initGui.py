class testPyFlow (Workbench):


    Icon = """
    /* XPM */
    static char * basic1_xpm[] = {
    "16 16 4 1",
    " 	c None",
    ".	c #FFFFFF",
    "@	c #e1350e",
    "#	c #074dd8",
    "......@@@@......",
    "......@##@......",
    ".....@#@#@@.....",
    ".....@#@@#@.....",
    ".....@#.@#@.....",
    "....@#@..@#@....",
    "....@#@..@#@....",
    "...@@#...@#@....",
    "...@#@....##@...",
    "...@#@@@@@@#@...",
    "..@#########@...",
    "..@#@@@@@@@@#@..",
    "..@#@......@#@..",
    ".@#@.......@##@.",
    ".@@@........@@@.",
    "................"};
    """

    MenuText = "Animation"
    ToolTip = "Faire des animations"

    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        import testFunc
        from PySide import QtCore, QtGui
        import PyFlow # import here all the needed files that create your FreeCAD commands

        self.list = ["OpenPyFlowCmd"] # A list of command names created in the line above
        self.appendToolbar(str(QtCore.QT_TRANSLATE_NOOP("basic1", "basic1")), self.list)
        self.appendMenu(str(QtCore.QT_TRANSLATE_NOOP("basic1", "basic1")), self.list)
        self.appendMenu(str(QtCore.QT_TRANSLATE_NOOP("basic2", "basic2")), self.list)

       

Gui.addWorkbench(testPyFlow())