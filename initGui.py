class testPyFlow (Workbench):


    Icon = """
    /* XPM */
    static char * basic1_xpm[] = {
    "16 16 5 1",
    " 	c None",
    ".	c #FFFFFF",
    "+	c #000000",
    "@	c #7F4F00",
    "#	c #FFBF00",
    "................",
    "...++++++++++++.",
    "..+@#########++.",
    ".+@#########+@+.",
    ".+++++++++++@#+.",
    ".+#########+##+.",
    ".+###++####+##+.",
    ".+####+####+##+.",
    ".+####+####+##+.",
    ".+####+####+##+.",
    ".+####+####+##+.",
    ".+####+####+##+.",
    ".+###+++###+#@+.",
    ".+#########+@+..",
    ".++++++++++++...",
    "................"};
    """


    MenuText = "Mon test de l'interface"
    ToolTip = "A description of my workbench"
    Icon = """paste here the contents of a 16x16 xpm icon"""

    def Initialize(self):
        """This function is executed when FreeCAD starts"""
        import testFunc
        from PySide import QtCore, QtGui
        import PyFlow # import here all the needed files that create your FreeCAD commands

        self.list = ["OpenPyFlowCmd"] # A list of command names created in the line above
        self.appendToolbar(str(QtCore.QT_TRANSLATE_NOOP("Basic1", "Basic1")), self.list)
        self.appendMenu(str(QtCore.QT_TRANSLATE_NOOP("Basic1", "Basic1")), self.list)

       

Gui.addWorkbench(testPyFlow())