from PyFlow.Core import NodeBase
from PyFlow.Packages.AnimationFreeCAD.Class.Animation import Animation
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *

class NodeAnimation(NodeBase):
   def __init__(self, name):
      super().__init__(name)
      self.createInputPin("inExec","ExecPin", None, self.compute)
      self.sortieNode = self.createOutputPin("outExec", "ExecPin")
      self.objet = self.createInputPin("Object", "ObjectPin", DEFAULT_VALUE_OBJECT_PIN)
      self.createInputPin("Loop", "BoolPin")
      self.createInputPin("Round trip", "BoolPin")
      self.createOutputPin("Object use", "ObjectPin", DEFAULT_VALUE_OBJECT_PIN)
      self.createOutputPin("Final position", "VectorPin")
      self.mouvement = None

   def compute(self):       
      estBoucle = self.getData("Loop")        
      estAllerRetour = self.getData("Round trip") 
      self.animation = Animation(estBoucle, estAllerRetour, self)