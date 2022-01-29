from PyFlow.Core import NodeBase

class NodeAnimation(NodeBase):
     def __init__(self, name):
        super().__init__(name)
        self.createInputPin("inExec","ExecPin", None, self.execute)
        self.createOutputPin("outExec", "ExecPin")
        self.createInputPin("Objet", "StringPin")
        self.createInputPin("Duree deplacement", "IntPin", 1)
        self.createInputPin("Boucle", "BoolPin")
        self.createInputPin("Aller-retour", "BoolPin")