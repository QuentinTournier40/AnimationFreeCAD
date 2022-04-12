from PyFlow.UI.Tool.Tool import ShelfTool
from nine import str
from PyFlow.UI.Tool.Tool import ShelfTool
from PySide2 import QtGui


import os
scriptDir = os.path.dirname(os.path.realpath(__file__))

class ExportationVideo(ShelfTool):
  """docstring for StopperMouvements."""
  def __init__(self):
      super(ExportationVideo, self).__init__()

  @staticmethod
  def toolTip():
      return "Mets en pause tous les mouvements en cours"

  @staticmethod
  def getIcon():
      path = "../../../../icons/exportationVideo.png"
      return QtGui.QIcon(scriptDir + os.path.sep + path)

  @staticmethod
  def name():
      return str("L'exportation video")

  def do(self):
      Exportation.getInstance().lancer()
