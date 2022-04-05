from PyFlow.Packages.AnimationFreeCAD.Class.MouvementEnCours import MouvementEnCours
from PyFlow.Packages.AnimationFreeCAD.Class.Pile import Pile
from Qt.QtWidgets import *
import FreeCAD

class Coordonnees():
    __instance = None

    def __init__(self):
        if Coordonnees.__instance is not None:
            raise Exception("Utiliser la méthode get_instance() pour obtenir une instance de l'objet")
        Coordonnees.pileSuivante = Pile()
        Coordonnees.pilePrecedente = Pile()


    def getInstance():
        if Coordonnees.__instance is None:
            Coordonnees.__instance = Coordonnees()
        return Coordonnees.__instance

    def ajouterEtape(self):
        Coordonnees.pilePrecedente.empiler(self.etape())

    def etape(self):
        etapeCourante = [[],[],[]]
        for i in FreeCAD.ActiveDocument.Objects:
            etapeCourante[0].append(i.Label)
            etapeCourante[1].append(i.Placement.Base)
            etapeCourante[2].append(i.Placement.Rotation.Q)
        etapeCourante.append(MouvementEnCours.getInstance().getListeNodesCourant())
        return etapeCourante

    def positionnerEtape(self,monEtape):
        for i in range(0,len(monEtape[0])):
                monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(monEtape[0][i])[0]
                monObjet.Placement.Base = monEtape[1][i]
                monObjet.Placement.Rotation.Q = monEtape[2][i]
        """for mouvement in monEtape[3]:
            MouvementEnCours.getInstance().ajouterNode(mouvement)"""
        
    def etapePrecedente(self):
        if(not (Coordonnees.pilePrecedente.estVide())):
            Coordonnees.pileSuivante.empiler(self.etape())
            etape = Coordonnees.pilePrecedente.depiler()
            Coordonnees.getInstance().positionnerEtape(etape)

    def etapeSuivante(self):
        if(not (Coordonnees.pileSuivante.estVide())):
            Coordonnees.pilePrecedente.empiler(self.etape())
            etape  = Coordonnees.pileSuivante.depiler()
            Coordonnees.getInstance().positionnerEtape(etape)