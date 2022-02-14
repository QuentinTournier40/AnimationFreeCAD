from PyFlow.Core import NodeBase

class NodeAnimation(NodeBase):
     def __init__(self, name):
        super().__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.compute)
        self.sortieNode = self.createOutputPin("outExec", "ExecPin")
        self.objet = self.createInputPin("Objet", "StringPin")
        self.estBoucle = self.createInputPin("Boucle", "BoolPin")
        self.estAllerRetour = self.createInputPin("Aller-retour", "BoolPin")
        self.positionFinale = self.createOutputPin("Position finale", "VectorPin")