from PyFlow.Core import NodeBase
from PyFlow.Packages.Dalmau.Class.Animation import Animation
from PyFlow.Packages.Dalmau.Class.Mouvement import *

class NodeAnimation(NodeBase):
   def __init__(self, name):
      super().__init__(name)
      self.createInputPin("inExec","ExecPin", None, self.compute)
      self.sortieNode = self.createOutputPin("outExec", "ExecPin")
      self.objet = self.createInputPin("Objet", "ObjectPin", DEFAULT_VALUE_OBJECT_PIN)
      self.createInputPin("Boucle", "BoolPin")
      self.createInputPin("Aller-retour", "BoolPin")
      self.createOutputPin("Objet use", "ObjectPin", DEFAULT_VALUE_OBJECT_PIN)
      self.createOutputPin("Position finale", "VectorPin")
      self.mouvement = None

   def compute(self):       
      estBoucle = self.getData("Boucle")        
      estAllerRetour = self.getData("Aller-retour") 
      self.animation = Animation(estBoucle, estAllerRetour, self)