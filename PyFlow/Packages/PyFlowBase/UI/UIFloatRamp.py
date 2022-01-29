## Copyright 2015-2019 Ilgar Lunin, Pedro Cabrera

## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at

##     http://www.apache.org/licenses/LICENSE-2.0

## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.


import weakref
from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets
from PyFlow.UI.Canvas.Painters import NodePainter
from PyFlow.UI.Canvas.UINodeBase import UINodeBase
from PyFlow.UI.Widgets.QtSliders import pyf_RampSpline


class UIFloatRamp(UINodeBase):
    def __init__(self, raw_node):
        super(UIFloatRamp, self).__init__(raw_node)
        self.selectors = []
        self.ramps = []

    def changeCurveType(self, index):
        self._rawNode._curveType = index
        for ramp in self.ramps:
            if ramp() is not None:
                ramp().setBezier(self._rawNode._curveTypes[self._rawNode._curveType] == "bezier")
                ramp().updateFromRaw()
        for selector in self.selectors:
            if selector() is not None:
                selector().setCurrentIndex(index)

    def rampChanged(self, tick=None):
        for ramp in self.ramps:
            if ramp() is not None:
                ramp().updateFromRaw()

    def createInputWidgets(self, inputsCategory, inGroup=None, pins=True):
        preIndex = inputsCategory.Layout.count()
        if pins:
            super(UIFloatRamp, self).createInputWidgets(inputsCategory, inGroup)
            inputVal = inputsCategory.getWidgetByName("input")
            if not self._rawNode.input.isArray():
                inputVal.setMinimum(0.0)
                inputVal.setMaximum(1.0)
        ramp = pyf_RampSpline(self._rawNode.ramp, bezier=self._rawNode._curveTypes[self._rawNode._curveType] == "bezier")
        ramp.tickClicked.connect(self.rampChanged)
        ramp.tickAdded.connect(self.rampChanged)
        ramp.tickRemoved.connect(self.rampChanged)
        ramp.tickMoved.connect(self.rampChanged)
        rampRef = weakref.ref(ramp)
        self.ramps.append(rampRef)
        selector = QtWidgets.QComboBox()
        selectorRef = weakref.ref(selector)
        self.selectors.append(selectorRef)
        for i in self._rawNode._curveTypes:
            selector.addItem(i)
        selector.setCurrentIndex(self._rawNode._curveType)
        selector.activated.connect(self.changeCurveType)
        inputsCategory.insertWidget(preIndex, "CurveType", selector,group=inGroup)
        inputsCategory.insertWidget(preIndex+1, "Ramp", ramp,group=inGroup)
