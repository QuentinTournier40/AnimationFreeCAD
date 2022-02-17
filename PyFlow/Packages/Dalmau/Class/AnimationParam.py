from PyFlow.Packages.Dalmau.Class.Mouvement import FenetreErreur

class AnimationParam():
    def __init__(self, uneDuree, estBoucle, estAllerRetour, nomNode):
        if(uneDuree <= 0):
            return FenetreErreur("Erreur", nomNode , "La durée ne peut pas être inférieure ou égale à 0.")
        self.duree = uneDuree
        self.estBoucle = estBoucle
        self.estAllerRetour = estAllerRetour