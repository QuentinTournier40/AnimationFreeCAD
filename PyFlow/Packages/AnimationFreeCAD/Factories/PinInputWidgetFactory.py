from PyFlow.Core.Common import *
from PyFlow.Core.Common import *
from PyFlow.UI.Widgets.InputWidgets import *
from PyFlow.UI.Widgets.QtSliders import *
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import DEFAULT_VALUE_OBJECT_PIN
from Qt import QtCore
from Qt.QtWidgets import *

import FreeCAD

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

class MyQComboBox(QtWidgets.QComboBox):
    def __init__(self, scrollWidget = None, *args, **kwargs):
        super(MyQComboBox, self).__init__(*args, **kwargs)
        self.scrollWidget = scrollWidget
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

    def wheelEvent(self, *args, **kwargs):
        if self.hasFocus():
            return QtGui.QComboBox.wheelEvent(self, *args, **kwargs)
        else:
            return self.scrollWidget.wheelEvent(*args, **kwargs)                


class LabelInputWidget(InputWidgetRaw):
    def __init__(self, **kwds):
        super(LabelInputWidget, self).__init__(**kwds)
        self.setLayout(QtWidgets.QHBoxLayout(self))
        self.combo = MyQComboBox()  
        self.populateCombo()
        self.combo.currentTextChanged.connect(self._onDataChangedComboBox)
        self.layout().addWidget(self.combo)

    @staticmethod
    def populateCombo(self):
        pass

    def blockWidgetSignals(self, bLocked):
        self.combo.blockSignals(bLocked)
    
    def _onDataChangedComboBox(self, val):
        self.dataSetCallback(val)
    
    def setWidgetValue(self, val):
        if(len(FreeCAD.ActiveDocument.getObjectsByLabel(val)) == 0 and val != DEFAULT_VALUE_OBJECT_PIN):
            self._onDataChangedComboBox(DEFAULT_VALUE_OBJECT_PIN)
        else:
            self.combo.setCurrentText(val)

class ObjectInputWidget(LabelInputWidget):
    def __init__(self, **kwds):
        super(ObjectInputWidget, self).__init__(**kwds)
        
    def populateCombo(self):
        objects = FreeCAD.ActiveDocument.Objects
        liste = []
        if(len(objects) != 0):
            for object in objects:
                liste.append(object.Label)
            liste.sort()           
            liste.insert(0, DEFAULT_VALUE_OBJECT_PIN)
            self.combo.addItems(liste)
        else:
            liste.append(DEFAULT_VALUE_OBJECT_PIN)
            self.combo.addItems(liste)

class CurveInputWidget(LabelInputWidget):
    def __init__(self, **kwds):
        super(CurveInputWidget, self).__init__(**kwds)
        
    def populateCombo(self):
        objects = FreeCAD.ActiveDocument.Objects
        liste = []
        if(len(objects) != 0):
            for object in objects:
                if(self.has_method(object.Shape, "discretize")):
                    liste.append(object.Label)
            liste.sort()           
            liste.insert(0, DEFAULT_VALUE_OBJECT_PIN)
            self.combo.addItems(liste)
        else:
            liste.append(DEFAULT_VALUE_OBJECT_PIN)
            self.combo.addItems(liste)

    def has_method(self, o, name):
        return callable(getattr(o, name, None)) 
    
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
        for i in [self.x, self.y, self.z]:
            i.blockSignals(bLocked)

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
    if dataType == 'ObjectPin':
        return ObjectInputWidget(dataSetCallback=dataSetter, defaultValue=defaultValue, **kwds)
    if dataType == 'CurvePin':
        return CurveInputWidget(dataSetCallback=dataSetter, defaultValue=defaultValue, **kwds)