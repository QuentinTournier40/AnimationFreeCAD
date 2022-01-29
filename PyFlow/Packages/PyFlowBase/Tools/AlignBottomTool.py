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


from nine import str
from PyFlow.UI.Tool.Tool import ShelfTool
from PyFlow.Packages.PyFlowBase.Tools import RESOURCES_DIR
from PyFlow.Core.Common import Direction

from Qt import QtGui
from Qt.QtWidgets import QFileDialog


class AlignBottomTool(ShelfTool):
    """docstring for AlignBottomTool."""
    def __init__(self):
        super(AlignBottomTool, self).__init__()

    @staticmethod
    def toolTip():
        return "Aligns selected nodes by bottom most node"

    @staticmethod
    def getIcon():
        return QtGui.QIcon(RESOURCES_DIR + "alignbottom.png")

    @staticmethod
    def name():
        return str("AlignBottomTool")

    def do(self):
        self.pyFlowInstance.getCanvas().alignSelectedNodes(Direction.Down)
