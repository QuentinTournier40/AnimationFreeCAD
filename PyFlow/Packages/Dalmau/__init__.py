PACKAGE_NAME = 'Dalmau'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Pins
from PyFlow.Packages.Dalmau.Pins.VectorPin import VectorPin 

# Function based nodes
from PyFlow.Packages.Dalmau.FunctionLibraries.VectorLib import VectorLib

# Class based nodes
from PyFlow.Packages.Dalmau.Nodes.TranslationRectiligneNode import TranslationRectiligneNode
from PyFlow.Packages.Dalmau.Nodes.TranslationRectiligneVitesseNode import TranslationRectiligneVitesseNode
from PyFlow.Packages.Dalmau.Nodes.TranslationAvecCourbeNode import TranslationAvecCourbeNode
from PyFlow.Packages.Dalmau.Nodes.TranslationAvecCourbeVitesseNode import TranslationAvecCourbeVitesseNode
from PyFlow.Packages.Dalmau.Nodes.RotationSurSoiMemeNode import RotationSurSoiMemeNode
from PyFlow.Packages.Dalmau.Nodes.RotationSurSoiMemeVitesseNode import RotationSurSoiMemeVitesseNode
from PyFlow.Packages.Dalmau.Nodes.RotationNode import RotationNode
from PyFlow.Packages.Dalmau.Nodes.RotationVitesseNode import RotationVitesseNode
from PyFlow.Packages.Dalmau.Nodes.getVectorValueNode import getVectorValue
from PyFlow.Packages.Dalmau.Nodes.PlacerNode import PlacerNode
from PyFlow.Packages.Dalmau.Nodes.setAngleObjectNode import setAngleObjectNode
from PyFlow.Packages.Dalmau.Nodes.CommencerNode import CommencerNode 

# Tools
from PyFlow.Packages.Dalmau.Tools.StopperMouvements import StopperMouvements
from PyFlow.Packages.Dalmau.Tools.ContinuerMouvements import ContinuerMouvements
from PyFlow.Packages.Dalmau.Tools.DemoDockTool import DemoDockTool

# Exporters
from PyFlow.Packages.Dalmau.Exporters.DemoExporter import DemoExporter

# Factories
from PyFlow.Packages.Dalmau.Factories.PinInputWidgetFactory import getInputWidget
# Prefs widgets
from PyFlow.Packages.Dalmau.PrefsWidgets.DemoPrefs import DemoPrefs

_FOO_LIBS = {
	VectorLib.__name__: VectorLib(PACKAGE_NAME)
}
_NODES = {
	TranslationRectiligneNode.__name__: TranslationRectiligneNode,
	TranslationAvecCourbeNode.__name__: TranslationAvecCourbeNode,
	RotationSurSoiMemeNode.__name__: RotationSurSoiMemeNode,
	CommencerNode.__name__: CommencerNode,
	RotationNode.__name__: RotationNode,
	getVectorValue.__name__: getVectorValue,
	PlacerNode.__name__: PlacerNode,
	setAngleObjectNode.__name__: setAngleObjectNode,
	TranslationRectiligneVitesseNode.__name__: TranslationRectiligneVitesseNode,
	TranslationAvecCourbeVitesseNode.__name__: TranslationAvecCourbeVitesseNode,
	RotationSurSoiMemeVitesseNode.__name__: RotationSurSoiMemeVitesseNode,
	RotationVitesseNode.__name__: RotationVitesseNode
}
_PINS = {
	VectorPin.__name__: VectorPin
}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()

_TOOLS[StopperMouvements.__name__] = StopperMouvements
_TOOLS[ContinuerMouvements.__name__] = ContinuerMouvements
_TOOLS[DemoDockTool.__name__] = DemoDockTool

_EXPORTERS[DemoExporter.__name__] = DemoExporter

_PREFS_WIDGETS["Demo"] = DemoPrefs


class Dalmau(IPackage):
	def __init__(self):
		super(Dalmau, self).__init__()

	@staticmethod
	def GetExporters():
		return _EXPORTERS

	@staticmethod
	def GetFunctionLibraries():
		return _FOO_LIBS

	@staticmethod
	def GetNodeClasses():
		return _NODES

	@staticmethod
	def GetPinClasses():
		return _PINS

	@staticmethod
	def GetToolClasses():
		return _TOOLS

	@staticmethod
	def PinsInputWidgetFactory():
		return getInputWidget

	@staticmethod
	def PrefsWidgets():
		return _PREFS_WIDGETS

