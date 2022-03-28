from PyFlow.Packages.AnimationFreeCAD.Class.NodeCourant import NodeCourant


class Animation():
    def __init__(self, estBoucle, estAllerRetour, node):
        self.estBoucle = estBoucle
        self.estAllerRetour = estAllerRetour
        self.sortieNode = node.sortieNode

    def executionDuree(self, unMouvement, unObjet, uneDuree):
        unMouvement.calculTrajectoire(self.estAllerRetour, uneDuree)
        unMouvement.setObjet(unObjet)
        if(NodeCourant.getInstance().isEnCours(unMouvement) == False):
            if(self.estBoucle and self.estAllerRetour):
                unMouvement.executionBoucleAllerRetour()
            elif(self.estBoucle and  not self.estAllerRetour):
                unMouvement.executionAllerBoucle()
            elif(not self.estBoucle and self.estAllerRetour):
                unMouvement.executionAllerRetour("")
            else:
                unMouvement.executionAller("") 

    def executionVitesse(self, unMouvement, unObjet, uneVitesse):
        duree = unMouvement.calculDuree(uneVitesse)
        unMouvement.calculTrajectoire(self.estAllerRetour, duree)
        unMouvement.setObjet(unObjet)
        if(self.estBoucle and self.estAllerRetour):
            unMouvement.executionBoucleAllerRetour()
        elif(self.estBoucle and  not self.estAllerRetour):
            unMouvement.executionAllerBoucle()
        elif(not self.estBoucle and self.estAllerRetour):
            unMouvement.executionAllerRetour("")
        else:
            unMouvement.executionAller("")       