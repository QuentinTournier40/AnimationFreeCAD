PACKAGE_NAME = 'AnimationFreeCAD'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Pins
from PyFlow.Packages.AnimationFreeCAD.Pins.VectorPin import VectorPin
from PyFlow.Packages.AnimationFreeCAD.Pins.ObjectPin import ObjectPin
from PyFlow.Packages.AnimationFreeCAD.Pins.CurvePin import CurvePin

# Function based nodes
from PyFlow.Packages.AnimationFreeCAD.FunctionLibraries.VectorLib import VectorLib

# Class based nodes
from PyFlow.Packages.AnimationFreeCAD.Nodes.TranslationRectiligneNode import TranslationRectiligneNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.TranslationRectiligneVitesseNode import TranslationRectiligneVitesseNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.TranslationAvecCourbeNode import TranslationAvecCourbeNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.TranslationAvecCourbeVitesseNode import TranslationAvecCourbeVitesseNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.RotationSurSoiMemeNode import RotationSurSoiMemeNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.RotationSurSoiMemeVitesseNode import RotationSurSoiMemeVitesseNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.RotationNode import RotationNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.RotationVitesseNode import RotationVitesseNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.getVectorValueNode import getVectorValue
from PyFlow.Packages.AnimationFreeCAD.Nodes.PlacerNode import PlacerNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.setAngleObjectNode import setAngleObjectNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.CommencerNode import CommencerNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.testFonctionNode import testFonctionNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.testNode import testNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.testAccelerer import testAccelerer
#from PyFlow.Packages.AnimationFreeCAD.Nodes.testDecelerer import testDecelerer
from PyFlow.Packages.AnimationFreeCAD.Nodes.Attendre import Attendre

# Tools
from PyFlow.Packages.AnimationFreeCAD.Tools.MettreEnPause import MettreEnPause
from PyFlow.Packages.AnimationFreeCAD.Tools.ContinuerMouvements import ContinuerMouvements
from PyFlow.Packages.AnimationFreeCAD.Tools.ResetPosition import ResetPosition
from PyFlow.Packages.AnimationFreeCAD.Tools.AjouterEtape import AjouterEtape
from PyFlow.Packages.AnimationFreeCAD.Tools.EtapePrecedente import EtapePrecedente
from PyFlow.Packages.AnimationFreeCAD.Tools.EtapeSuivante import EtapeSuivante
from PyFlow.Packages.AnimationFreeCAD.Tools.ArreterTousLesMouvements import ArreterTousLesMouvements 
from PyFlow.Packages.AnimationFreeCAD.Tools.ExportationVideo import ExportationVideo 
from PyFlow.Packages.AnimationFreeCAD.Tools.DemoDockTool import DemoDockTool

# Exporters
from PyFlow.Packages.AnimationFreeCAD.Exporters.DemoExporter import DemoExporter

# Factories
from PyFlow.Packages.AnimationFreeCAD.Factories.PinInputWidgetFactory import getInputWidget
# Prefs widgets
from PyFlow.Packages.AnimationFreeCAD.PrefsWidgets.DemoPrefs import DemoPrefs

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
	RotationVitesseNode.__name__: RotationVitesseNode,
	testFonctionNode.__name__: testFonctionNode,
	testNode.__name__: testNode,
	testAccelerer.__name__: testAccelerer,
	Attendre.__name__: Attendre
}
_PINS = {
	VectorPin.__name__: VectorPin,
	ObjectPin.__name__: ObjectPin,
	CurvePin.__name__: CurvePin
}
_TOOLS = OrderedDict()
_PREFS_WIDGETS = OrderedDict()
_EXPORTERS = OrderedDict()

_TOOLS[MettreEnPause.__name__] = MettreEnPause
_TOOLS[ContinuerMouvements.__name__] = ContinuerMouvements
_TOOLS[ArreterTousLesMouvements.__name__] = ArreterTousLesMouvements
_TOOLS[ResetPosition.__name__] = ResetPosition
_TOOLS[AjouterEtape.__name__] = AjouterEtape
_TOOLS[EtapePrecedente.__name__] = EtapePrecedente
_TOOLS[EtapeSuivante.__name__] = EtapeSuivante 
_TOOLS[ExportationVideo.__name__] = ExportationVideo 
_TOOLS[DemoDockTool.__name__] = DemoDockTool

_EXPORTERS[DemoExporter.__name__] = DemoExporter

_PREFS_WIDGETS["Demo"] = DemoPrefs


class AnimationFreeCAD(IPackage):
	def __init__(self):
		super(AnimationFreeCAD, self).__init__()

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

