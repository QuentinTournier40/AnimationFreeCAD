PACKAGE_NAME = 'AnimationFreeCAD'

from collections import OrderedDict
from PyFlow.UI.UIInterfaces import IPackage

# Pins
from PyFlow.Packages.AnimationFreeCAD.Pins.VectorPin import VectorPin
from PyFlow.Packages.AnimationFreeCAD.Pins.ObjectPin import ObjectPin
from PyFlow.Packages.AnimationFreeCAD.Pins.CurvePin import CurvePin

# Function based nodes

# Class based nodes
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.TranslationRectiligneNode import TranslationRectiligneNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.TranslationRectiligneVitesseNode import TranslationRectiligneVitesseNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.TranslationAvecCourbeNode import TranslationAvecCourbeNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.TranslationAvecCourbeVitesseNode import TranslationAvecCourbeVitesseNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.RotationSurSoiMemeNode import RotationSurSoiMemeNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.RotationSurSoiMemeVitesseNode import RotationSurSoiMemeVitesseNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.RotationNode import RotationNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.RotationVitesseNode import RotationVitesseNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.getValeurVecteurNode import getValeurVecteurNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.PlacerNode import PlacerNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.setAngleObjetNode import setAngleObjetNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.CommencerNode import CommencerNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.FonctionMathNode import FonctionMathNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.TranslationAccelere import TranslationAccelere
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.TranslationDecelere import TranslationDecelere
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.Attendre import Attendre
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.CreateVecteurNode import CreateVecteurNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.MakeVecteurNode import MakeVecteurNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.RotationXNode import RotationXNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.RotationYNode import RotationYNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.RotationZNode import RotationZNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.GetPlacement import GetPlacement
from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.Avancer import AvancerNode

from PyFlow.Packages.AnimationFreeCAD.Nodes.en.RectilinearTranslationNode import RectilinearTranslationNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.RectilinearTranslationBySpeedNode import RectilinearTranslationBySpeedNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.TranslationWithCurveNode import TranslationWithCurveNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.TranslationWithCurveBySpeedNode import TranslationWithCurveBySpeedNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.SpinAroundNode import SpinAroundNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.SpinAroundBySpeedNode import SpinAroundBySpeedNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.SpinNode import SpinNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.SpinBySpeedNode import SpinBySpeedNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.getVectorValueNode import getVectorValue
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.PlaceNode import PlaceNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.setAngleObjectNode import setAngleObjectNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.StartNode import StartNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.AcceleratesTranslationNode import AcceleratesTranslationNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.DeceleratesTranslationNode import DeceleratesTranslationNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.WaitNode import WaitNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.CreateVectorNode import CreateVectorNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.MakeVectorNode import MakeVectorNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.MathTranslation import MathTranslation
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.SpinXNode import SpinXNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.SpinYNode import SpinYNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.SpinZNode import SpinZNode
from PyFlow.Packages.AnimationFreeCAD.Nodes.en.GetPosition import GetPosition

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
}

_NODES = {
	TranslationRectiligneNode.__name__: TranslationRectiligneNode,
	TranslationAvecCourbeNode.__name__: TranslationAvecCourbeNode,
	RotationSurSoiMemeNode.__name__: RotationSurSoiMemeNode,
	CommencerNode.__name__: CommencerNode,
	RotationNode.__name__: RotationNode,
	getValeurVecteurNode.__name__: getValeurVecteurNode,
	PlacerNode.__name__: PlacerNode,
	setAngleObjetNode.__name__: setAngleObjetNode,
	TranslationRectiligneVitesseNode.__name__: TranslationRectiligneVitesseNode,
	TranslationAvecCourbeVitesseNode.__name__: TranslationAvecCourbeVitesseNode,
	RotationSurSoiMemeVitesseNode.__name__: RotationSurSoiMemeVitesseNode,
	RotationVitesseNode.__name__: RotationVitesseNode,
	FonctionMathNode.__name__: FonctionMathNode,
	TranslationDecelere.__name__: TranslationDecelere,
	TranslationAccelere.__name__: TranslationAccelere,
	Attendre.__name__: Attendre,
	CreateVecteurNode.__name__: CreateVecteurNode,
	MakeVecteurNode.__name__: MakeVecteurNode,
	RotationXNode.__name__: RotationXNode,
	RotationYNode.__name__: RotationYNode,
	RotationZNode.__name__: RotationZNode,
	GetPlacement.__name__: GetPlacement,
	AvancerNode.__name__: AvancerNode,
	
	RectilinearTranslationNode.__name__: RectilinearTranslationNode,
	RectilinearTranslationBySpeedNode.__name__: RectilinearTranslationBySpeedNode,
	TranslationWithCurveNode.__name__: TranslationWithCurveNode,
	TranslationWithCurveBySpeedNode.__name__: TranslationWithCurveBySpeedNode,
	SpinAroundNode.__name__: SpinAroundNode,
	SpinAroundBySpeedNode.__name__: SpinAroundBySpeedNode,
	SpinNode.__name__: SpinNode,
	SpinBySpeedNode.__name__: SpinBySpeedNode,
	getVectorValue.__name__: getVectorValue,
	PlaceNode.__name__: PlaceNode,
	setAngleObjectNode.__name__: setAngleObjectNode,
	StartNode.__name__: StartNode,
	AcceleratesTranslationNode.__name__: AcceleratesTranslationNode,
	DeceleratesTranslationNode.__name__: DeceleratesTranslationNode,
	WaitNode.__name__: WaitNode,
	CreateVectorNode.__name__: CreateVectorNode,
	MakeVectorNode.__name__: MakeVectorNode,
  MathTranslation.__name__: MathTranslation,
  SpinXNode.__name__: SpinXNode,
  SpinYNode.__name__: SpinYNode,
  SpinZNode.__name__: SpinZNode,
  GetPosition.__name__: GetPosition
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

