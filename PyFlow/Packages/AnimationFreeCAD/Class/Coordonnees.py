from PyFlow.Packages.AnimationFreeCAD.Class.NodeCourant import NodeCourant
from PyFlow.Packages.AnimationFreeCAD.Class.Pile import Pile
from Qt.QtWidgets import *
import FreeCAD

class Coordonnees():
    __instance = None
    pileSuivant = Pile()
    pilePrecedent = Pile()
    listePlacementsMouvements = [[],[],[]]
    listeMouvementsCourants = []
    etapeCourante = []
    listeAngles = []
    replay = False          #Dès qu'on appuie sur précédent ou suivant, passe en true pour savoir si on a cliqué

    def __init__(self):
        if Coordonnees.__instance is not None:
            raise Exception("Utiliser la méthode get_instance() pour obtenir une instance de l'objet")
        Coordonnees.listePlacementsMouvements = [[],[],[]]

    def getInstance():
        if Coordonnees.__instance is None:
            Coordonnees.__instance = Coordonnees()
        return Coordonnees.__instance
    
    def recuperation(self):
        for i in FreeCAD.ActiveDocument.Objects:
            self.listePlacementsMouvements[0].append(i.Label)
            self.listePlacementsMouvements[1].append(i.Placement.Base)
            self.listeAngles.append(i.Placement.Rotation.Q)
            #print("Enregistrement des coordonnées de l'objet :" + i.Label)

    def positionner(self):
        for i in range(len(self.listePlacementsMouvements[0])):
            monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(Coordonnees.listePlacementsMouvements[0][i])[0]
            #print("Position reset :" + Coordonnees.listePlacementsMouvements[0][i])
            monObjet.Placement.Base = Coordonnees.listePlacementsMouvements[1][i]
            monObjet.Placement.Rotation.Q = Coordonnees.listeAngles[i]

    def positionnerEtape(self,monEtape):
        for i in range(0,len(monEtape[0])):
                monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(monEtape[0][i])[0]  #on récupère l'objet
                monObjet.Placement.Base = monEtape[1][i]        #on le remet à ses coordonnées (x,y,z)
                #print("Valeur de monEtape[1][i] : ")
                #print(monEtape[1][i])
                monObjet.Placement.Rotation.Q = monEtape[2][i]        #on le repositionne avec son angle
                #print("Valeur de monEtape[2][i] : ")
                #print(monEtape[2][i])

    def ajouterEtape(self):
        monEtape = [[],[],[],[]]
        for i in FreeCAD.ActiveDocument.Objects:        #enregistre le nom et les paramètres de placement / rotation de chaque objet
            monEtape[0].append(i.Label)
            monEtape[1].append(i.Placement.Base)
            monEtape[2].append(i.Placement.Rotation.Q)
        monEtape[3].append(NodeCourant.getInstance().getListeNodeCourant())
        self.listeMouvementsCourants = NodeCourant.getInstance().getListeNodeCourant()
        self.pilePrecedent.empiler(monEtape)
        #print(monEtape)
        
    def etapePrecedente(self):
        if(self.pilePrecedent.estVide()):
            #print("Il n'existe pas d'étape précédente")
            pass
        else:
            self.replay = True
            self.etapeCourante = self.pilePrecedent.lireSommet()
            self.listeMouvementsCourants = self.etapeCourante[3]
            self.pileSuivant.empiler(self.etapeCourante)
            self.pilePrecedent.depiler()
            self.positionnerEtape(self.etapeCourante)
            #print("======Affichage des mouvements courants======")
            #print(self.listeMouvementsCourants)
            NodeCourant.getInstance().enleverTousLesMouvements()
            for mouvement in self.listeMouvementsCourants:
                NodeCourant.getInstance().ajouterNode(mouvement)

    def etapeSuivante(self):
        if(self.pileSuivant.estVide()):
            #print("Il n'exite pas d'étape suivante")
            pass
        else:
            self.replay = True
            self.etapeCourante = self.pileSuivant.lireSommet()
            self.listeMouvementsCourants = self.etapeCourante[3]
            self.pilePrecedent.empiler(self.etapeCourante)
            self.pileSuivant.depiler()
            self.positionnerEtape(self.etapeCourante)
            #print("======Affichage des mouvements courants======")
            #print(self.listeMouvementsCourants)
            NodeCourant.getInstance().enleverTousLesMouvements()
            for mouvement in self.listeMouvementsCourants:
                NodeCourant.getInstance().ajouterNode(mouvement)