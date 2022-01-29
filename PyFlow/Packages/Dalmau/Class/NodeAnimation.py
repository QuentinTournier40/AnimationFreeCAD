from PyFlow.Core import NodeBase

class NodeAnimation(NodeBase):
     def __init__(self, name):
        super().__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.compute)
        self.createOutputPin("outExec", "ExecPin")
        self.createInputPin("Objet", "StringPin")
        self.createInputPin("Duree deplacement", "IntPin")
        self.createInputPin("Realiser en boucle ?", "BoolPin")
        self.createInputPin("Realiser en aller-retour", "BoolPin")