class MouvementEnCours:
    __instance = None

    def __init__(self):
        if MouvementEnCours.__instance is not None:
            raise Exception(
                "Utiliser la méthode get_instance() pour obtenir une instance de l'objet")
        MouvementEnCours.__listeMouvementEnCours = []

    def getInstance():
        if MouvementEnCours.__instance is None:
            MouvementEnCours.__instance = MouvementEnCours()

        return MouvementEnCours.__instance

    def ajouterNode(self, unMouvement):
        MouvementEnCours.__listeMouvementEnCours.append(unMouvement)

    def enleverNode(self, unMouvement):
        MouvementEnCours.__listeMouvementEnCours.pop(
            MouvementEnCours.__listeMouvementEnCours.index(unMouvement))

    def mettreEnPause(self):
        for mouvement in self.__listeMouvementEnCours:
            mouvement.mettreEnPause()

    def continuerNodesCourant(self):
        for mouvement in self.__listeMouvementEnCours:
            mouvement.activerMouvement()

    def arreterLAnimation(self):
        MouvementEnCours.getInstance().mettreEnPause()
        for i in range(0, len(self.__listeMouvementEnCours)):
            del(self.__listeMouvementEnCours[0])

    def isEnCours(self, unMouvement):
        resultat = False
        for mouvement in self.__listeMouvementEnCours:
            if(mouvement.memeMouvement(unMouvement)):
                resultat = True
                break
        return resultat

    def getListeNodesCourant(self):
        return MouvementEnCours.__listeMouvementEnCours