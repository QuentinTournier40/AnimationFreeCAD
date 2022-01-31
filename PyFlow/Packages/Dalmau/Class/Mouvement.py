from abc import ABC, abstractmethod

class Mouvement(ABC):
    def __init__(self, unNode, unObjet, uneDuree, estBoucle, estAllerRetour):
        self.node = unNode
        self.objet = unObjet
        self.duree = uneDuree
        self.estBoucle = estBoucle
        self.estAllerRetour = estAllerRetour
        self.etape = 0
        self.premiereEtapeAllerRetour = True

    @abstractmethod
    def repetitionMouvement(self, unTimer):
        pass

    @abstractmethod
    def repetitionMouvementSansFin(self, unTimer):
        pass

    @abstractmethod
    def repetitionMouvementAllerRetour(self, unTimer):
        pass

    @abstractmethod
    def repetitionMouvementSansFinEtAllerRetour(self, unTimer):
        pass  