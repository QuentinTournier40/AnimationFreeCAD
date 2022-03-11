class NodeCourant:
    __instance = None
    __listeNodeCourant = []
    
    def __init__(self):
        if NodeCourant.__instance is not None :
            raise Exception("Utiliser la méthode get_instance() pour obtenir une instance de l'objet")
        NodeCourant.__listeNodeCourant = []

    def getInstance():
        if NodeCourant.__instance is None:
            NodeCourant.__instance = NodeCourant()
        return NodeCourant.__instance

    def ajouterNode(self,unMouvement):
        NodeCourant.__listeNodeCourant.append(unMouvement)

    def enleverNode(self,unMouvement):
        print(NodeCourant.__listeNodeCourant.index(unMouvement))
        NodeCourant.__listeNodeCourant.pop(NodeCourant.__listeNodeCourant.index(unMouvement))

    def stopperNodesCourant(self):
        for mouvement in self.__listeNodeCourant:
            mouvement.stopperMouvement()
    
    def continuerNodesCourant(self):
        for mouvement in self.__listeNodeCourant:
            mouvement.activerMouvement()