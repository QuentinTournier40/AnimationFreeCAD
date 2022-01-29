from PyFlow.Core.Common import *
from Qt import QtCore
from Qt.QtWidgets import *
from PyFlow.Core.Common import *
from PyFlow.UI.Widgets.InputWidgets import *
from PyFlow.UI.Widgets.QtSliders import *
import FreeCAD

FLOAT_SINGLE_STEP = 0.01
FLOAT_DECIMALS = 5


class DemoInputWidget(InputWidgetSingle):
    """Boolean data input widget"""

    def __init__(self, parent=None, **kwds):
        super(DemoInputWidget, self).__init__(parent=parent, **kwds)
        self.cb = QCheckBox(self)
        self.setWidget(self.cb)
        self.cb.stateChanged.connect(lambda val: self.dataSetCallback(bool(val)))

    def blockWidgetSignals(self, bLocked):
        self.cb.blockSignals(bLocked)

    def setWidgetValue(self, val):
        if bool(val):
            self.cb.setCheckState(QtCore.Qt.Checked)
        else:
            self.cb.setCheckState(QtCore.Qt.Unchecked)

class VectorInputWidget(InputWidgetRaw):
    def __init__(self, **kwds):
        super(VectorInputWidget, self).__init__(**kwds)
        self.setLayout(QtWidgets.QGridLayout())
        self.x = valueBox(None, "float", True)
        self.y = valueBox(None, "float", True)
        self.z = valueBox(None, "float", True)
        self.labelX = QLabel("X :")
        self.labelY = QLabel("Y :")
        self.labelZ = QLabel("Z :")

        self.layout().addWidget(self.labelX, 1, 1)
        self.layout().addWidget(self.x, 1, 2)
        self.layout().addWidget(self.labelY, 2, 1)
        self.layout().addWidget(self.y, 2, 2)
        self.layout().addWidget(self.labelZ, 3, 1)
        self.layout().addWidget(self.z, 3, 2)

        self.layout().setColumnStretch(2, 1)

        self.x.valueChanged.connect(self._onDataChangedX)
        self.y.valueChanged.connect(self._onDataChangedY)
        self.z.valueChanged.connect(self._onDataChangedZ)

    def blockWidgetSignals(self, bLocked):
        try:
            for i in [self.x, self.y, self.z]:
                i.blockSignals(bLocked)
        except:
            pass

    def asDataTypeClass(self):
        return FreeCAD.Vector([self.x.value(), self.y.value(), self.z.value()])

    def _onDataChangedX(self, val):
        tmp = self.asDataTypeClass()
        tmp.x = val
        self.dataSetCallback(tmp)

    def _onDataChangedY(self, val):
        tmp = self.asDataTypeClass()
        tmp.y = val
        self.dataSetCallback(tmp)

    def _onDataChangedZ(self, val):
        tmp = self.asDataTypeClass()
        tmp.z = val
        self.dataSetCallback(tmp)

    def setWidgetValue(self, val):
        self.x.setValue(val.x)
        self.y.setValue(val.y)
        self.z.setValue(val.z)

def getInputWidget(dataType, dataSetter, defaultValue, widgetVariant=DEFAULT_WIDGET_VARIANT, **kwds):
    if dataType == 'DemoPin':
        return DemoInputWidget(dataSetCallback=dataSetter, defaultValue=defaultValue, **kwds)
    if dataType == 'VectorPin':
        return VectorInputWidget(dataSetCallback=dataSetter, defaultValue=defaultValue, **kwds)

