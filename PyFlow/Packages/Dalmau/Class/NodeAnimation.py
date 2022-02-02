from PyFlow.Core import NodeBase

class NodeAnimation(NodeBase):
     def __init__(self, name):
        super().__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.compute)
        self.createOutputPin("outExec", "ExecPin")
        self.objet = self.createInputPin("Objet", "StringPin")
        self.duree = self.createInputPin("Duree deplacement", "IntPin", 1)
        self.boucle = self.createInputPin("Boucle", "BoolPin")
        self.allerRetour = self.createInputPin("Aller-retour", "BoolPin")
        self.positionFinale = self.createOutputPin("Position finale", "VectorPin")