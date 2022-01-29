PACKAGE_NAME = 'Dalmau'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Pins
from PyFlow.Packages.Dalmau.Pins.DemoPin import DemoPin
from PyFlow.Packages.Dalmau.Pins.VectorPin import VectorPin 

# Function based nodes
from PyFlow.Packages.Dalmau.FunctionLibraries.DemoLib import DemoLib
from PyFlow.Packages.Dalmau.FunctionLibraries.TranslationLib import TranslationLib
from PyFlow.Packages.Dalmau.FunctionLibraries.RotationLib import RotationLib 
from PyFlow.Packages.Dalmau.FunctionLibraries.AutreLib import AutreLib

# Class based nodes
from PyFlow.Packages.Dalmau.Nodes.DemoNode import DemoNode
from PyFlow.Packages.Dalmau.Nodes.TranslationRectiligneSansCourbeNode import TranslationRectiligneSansCourbeNode
from PyFlow.Packages.Dalmau.Nodes.TranslationAvecCourbeNode import TranslationAvecCourbeNode 
from PyFlow.Packages.Dalmau.Nodes.RotationSurSoiMemeNode import RotationSurSoiMemeNode 
from PyFlow.Packages.Dalmau.Nodes.CommencerNode import CommencerNode 
from PyFlow.Packages.Dalmau.Nodes.RotationNode import RotationNode 

# Tools
from PyFlow.Packages.Dalmau.Tools.DemoShelfTool import DemoShelfTool
from PyFlow.Packages.Dalmau.Tools.DemoDockTool import DemoDockTool

# Exporters
from PyFlow.Packages.Dalmau.Exporters.DemoExporter import DemoExporter

# Factories
from PyFlow.Packages.Dalmau.Factories.UIPinFactory import createUIPin
from PyFlow.Packages.Dalmau.Factories.UINodeFactory import createUINode
from PyFlow.Packages.Dalmau.Factories.PinInputWidgetFactory import getInputWidget
# Prefs widgets
from PyFlow.Packages.Dalmau.PrefsWidgets.DemoPrefs import DemoPrefs

_FOO_LIBS = {
	TranslationLib.__name__: TranslationLib(PACKAGE_NAME),
	RotationLib.__name__: RotationLib(PACKAGE_NAME),
	AutreLib.__name__: AutreLib(PACKAGE_NAME)
}
_NODES = {
	TranslationRectiligneSansCourbeNode.__name__: TranslationRectiligneSansCourbeNode,
	TranslationAvecCourbeNode.__name__: TranslationAvecCourbeNode,
	RotationSurSoiMemeNode.__name__: RotationSurSoiMemeNode,
	CommencerNode.__name__: CommencerNode,
	RotationNode.__name__: RotationNode
}
_PINS = {
	VectorPin.__name__: VectorPin
}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()

_FOO_LIBS[DemoLib.__name__] = DemoLib(PACKAGE_NAME)

_NODES[DemoNode.__name__] = DemoNode

_PINS[DemoPin.__name__] = DemoPin

_TOOLS[DemoShelfTool.__name__] = DemoShelfTool
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
	def UIPinsFactory():
		return createUIPin

	@staticmethod
	def UINodesFactory():
		return createUINode

	@staticmethod
	def PinsInputWidgetFactory():
		return getInputWidget

	@staticmethod
	def PrefsWidgets():
		return _PREFS_WIDGETS

