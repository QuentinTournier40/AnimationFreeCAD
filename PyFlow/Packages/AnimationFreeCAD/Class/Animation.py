from PyFlow.Packages.AnimationFreeCAD.Class.MouvementEnCours import MouvementEnCours


class Animation():
    def __init__(self, estBoucle, estAllerRetour, node):
        self.estBoucle = estBoucle
        self.estAllerRetour = estAllerRetour
        self.sortieNode = node.sortieNode

    def executionDuree(self, unMouvement, unObjet, uneDuree):
        unMouvement.calculTrajectoire(self.estAllerRetour, uneDuree)
        self.execution(unMouvement, unObjet)

    def executionVitesse(self, unMouvement, unObjet, uneVitesse):
        duree = unMouvement.calculDuree(uneVitesse)
        unMouvement.calculTrajectoire(self.estAllerRetour, duree)
        self.execution(unMouvement, unObjet)

    def execution(self, unMouvement, unObjet):
        unMouvement.setObjet(unObjet)
        if(self.estBoucle and self.estAllerRetour):
            unMouvement.executionBoucleAllerRetour()
        elif(self.estBoucle and not self.estAllerRetour):
            unMouvement.executionAllerBoucle()
        elif(not self.estBoucle and self.estAllerRetour):
            unMouvement.executionAllerRetour()
        else:
            unMouvement.executionAller()
