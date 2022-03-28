from tabnanny import check
from nine import str
from Qt import QtGui
from Qt import QtCore
import FreeCAD


from PyFlow.UI.Tool.Tool import DockTool

from Qt.QtWidgets import QUndoView
from Qt.QtWidgets import QWidget
from Qt.QtWidgets import QCheckBox
from Qt.QtWidgets import QHBoxLayout
from Qt.QtWidgets import QLabel
from Qt.QtWidgets import QVBoxLayout
from Qt.QtWidgets import QPushButton
#from Qt.QtWidgets import QIntValidator
from Qt.QtWidgets import QLineEdit
from Qt.QtWidgets import *

class DemoDockTool(DockTool):
    """docstring for History tool."""
    def __init__(self):
        super(DemoDockTool, self).__init__()

        self.setMinimumSize(QtCore.QSize(200, 50))
        self.varsWidget = None
        self.content = QWidget()
        self.content.setObjectName("DemoToolContent")

        self.layout = QVBoxLayout(self.content)

        self.boutonStartAndStop = QPushButton("Démarrer l'animation",self.content)
        self.boutonArreter = QPushButton("Arrêter l'animation",self.content)

        self.etapePrecedente = QPushButton("Etape précédente",self.content)
        self.etapeSuivante = QPushButton("Etape suivante",self.content)

        self.labelEtape = QLabel(self)
        self.labelAvancement = QLabel(self)

        self.labelEtape.setText('Etape :')
        self.etape = QLineEdit(self)

        self.labelAvancement.setText('Avancement :')
        self.avancement = QLineEdit(self)

        #self.onlyInt = QIntValidator()
        #self.line.setValidator(self.onlyInt)   

        self.layout.addWidget(self.boutonStartAndStop)
        self.layout.addWidget(self.boutonArreter)

        self.layoutHorizontal1 = QHBoxLayout()
        self.layoutHorizontal2 = QHBoxLayout()
        self.layoutHorizontal3 = QHBoxLayout()

        self.layoutHorizontal1.addWidget(self.labelEtape)
        self.layoutHorizontal1.addWidget(self.etape)

        self.layoutHorizontal2.addWidget(self.labelAvancement)
        self.layoutHorizontal2.addWidget(self.avancement)

        self.layoutHorizontal3.addWidget(self.etapePrecedente)
        self.layoutHorizontal3.addWidget(self.etapeSuivante)

        self.layout.addLayout(self.layoutHorizontal1)
        self.layout.addLayout(self.layoutHorizontal2)
        self.layout.addLayout(self.layoutHorizontal3)
        # FreeCAD.Gui.runCommand('Std_ViewDockUndockFullscreen',1)

        self.setWidget(self.content)
        
        # self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        
    
    @staticmethod
    def getIcon():
        return QtGui.QIcon(":brick.png")

    def onShow(self):
        super(DemoDockTool, self).onShow()
        

    @staticmethod
    def toolTip():
        return "My awesome dock tool!"


    @staticmethod
    def name():
        return str("DemoDockTool")
