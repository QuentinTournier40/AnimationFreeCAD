class NodeCourant:
    __instance = None
    __listeNodeCourant = []
    
    def __init__(self):
        if NodeCourant.__instance is not None :
            raise Exception("Utiliser la méthode get_instance() pour obtenir une instance de l'objet")
        NodeCourant.__listeNodeCourant = []

    def getInstance():
        if NodeCourant.__instance is None:
            #print("Création de l'instance")
            NodeCourant.__instance = NodeCourant()
        else:
            #print("Déja créé")
            pass

        return NodeCourant.__instance

    def ajouterNode(self,unMouvement):
        NodeCourant.__listeNodeCourant.append(unMouvement)
        #print("Ajout node " + str(NodeCourant.__listeNodeCourant))

    def enleverNode(self,unMouvement):
        #print(NodeCourant.__listeNodeCourant.index(unMouvement))
        NodeCourant.__listeNodeCourant.pop(NodeCourant.__listeNodeCourant.index(unMouvement))
        #print("Enlever node " + str(self.__listeNodeCourant))

    def stopperNodesCourant(self):
        for mouvement in self.__listeNodeCourant:
            mouvement.stopperMouvement()
    
    def continuerNodesCourant(self):
        for mouvement in self.__listeNodeCourant:
            mouvement.activerMouvement()

    def arreterLAnimation(self):
        self.stopperNodesCourant()
        for i in range(0, len(self.__listeNodeCourant)):
            del(self.__listeNodeCourant[0])

    def isEnCours(self, unMouvement):
        resultat = False
        for mouvement in self.__listeNodeCourant:
            if(mouvement.memeMouvement(unMouvement)):
                resultat = True
                break
        #print(resultat)
        return resultat