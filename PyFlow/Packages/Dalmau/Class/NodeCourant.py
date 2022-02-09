class NodeCourant:
    __instance = None
    __listeNodeCourant = []
    
    def __init__(self):
        if NodeCourant.__instance is not None :
            raise Exception("Utiliser la méthode get_instance() pour obtenir une instance de l'objet")
        NodeCourant.__listeNodeCourant = []

    def getInstance():
        if NodeCourant.__instance is None:
            print("Création de l'instance")
            NodeCourant.__instance = NodeCourant()
        else:
            print("Déja créé")

        return NodeCourant.__instance


    def ajouterNode(self,unMouvement):
        NodeCourant.__listeNodeCourant.append(unMouvement)
        print("Ajout node ")


    def enleverNode(self,unMouvement):
        NodeCourant.__listeNodeCourant.pop(NodeCourant.__listeNodeCourant.index(unMouvement) - 1)
        print("Enlever node ")
