from lib2to3.pytree import Node
from PyFlow.Packages.Dalmau.Class.Mouvement import FenetreErreur
from PyFlow.Packages.Dalmau.Class.NodeCourant import NodeCourant


class Animation():
    def __init__(self, estBoucle, estAllerRetour, node):
        self.estBoucle = estBoucle
        self.estAllerRetour = estAllerRetour
        self.sortieNode = node.sortieNode

    def executionDuree(self, unMouvement, unObjet, uneDuree):
        unMouvement.calculTrajectoire(self.estAllerRetour, uneDuree)
        unMouvement.setObjet(unObjet)
        if(self.estBoucle and self.estAllerRetour):
            unMouvement.executionBoucleAllerRetour()
            #print("1")
        elif(self.estBoucle and  not self.estAllerRetour):
            unMouvement.executionAllerBoucle()
            #print("2")
        elif(not self.estBoucle and self.estAllerRetour):
            unMouvement.executionAllerRetour("")
            #print("3")
        else:
            unMouvement.executionAller("")
            #print("4")

    def executionVitesse(self, unMouvement, unObjet, uneVitesse):
        duree = unMouvement.calculDuree(uneVitesse)
        unMouvement.calculTrajectoire(self.estAllerRetour, duree)
        unMouvement.setObjet(unObjet)
        if(self.estBoucle and self.estAllerRetour):
            unMouvement.executionBoucleAllerRetour()
            #print("1")
        elif(self.estBoucle and  not self.estAllerRetour):
            unMouvement.executionAllerBoucle()
            #print("2")
        elif(not self.estBoucle and self.estAllerRetour):
            unMouvement.executionAllerRetour("")
            #print("3")
        else:
            unMouvement.executionAller("")
            #print("4")

    


        