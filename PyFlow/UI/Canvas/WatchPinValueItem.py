from PySide2 import QtCore
from PySide2 import QtGui

from PySide2.QtWidgets import *

from PyFlow.UI.Utils.stylesheet import editableStyleSheet
from PyFlow.Core.Common import *


class WatchItem(QGraphicsTextItem):
    """docstring for WatchItem."""
    def __init__(self, text=""):
        super(WatchItem, self).__init__(text)

    def paint(self, painter, option, widget):
        painter.drawRect(self.boundingRect())
        painter.fillRect(self.boundingRect(), editableStyleSheet().BgColor)
        super(WatchItem, self).paint(painter, option, widget)
