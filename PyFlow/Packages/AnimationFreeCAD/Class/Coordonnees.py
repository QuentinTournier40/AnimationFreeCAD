from PyFlow.Packages.AnimationFreeCAD.Class.MouvementEnCours import MouvementEnCours
from PyFlow.Packages.AnimationFreeCAD.Class.Pile import Pile
from Qt.QtWidgets import *
import FreeCAD


class Coordonnees():
    __instance = None

    def __init__(self):
        if Coordonnees.__instance is not None:
            raise Exception(
                "Utiliser la méthode get_instance() pour obtenir une instance de l'objet")
        Coordonnees.pileSuivante = Pile()
        Coordonnees.pilePrecedente = Pile()
        Coordonnees.etapeCourante = None

    def getInstance():
        if Coordonnees.__instance is None:
            Coordonnees.__instance = Coordonnees()
        return Coordonnees.__instance

    def ajouterEtape(self):
        if(Coordonnees.etapeCourante is not None):
            Coordonnees.pilePrecedente.empiler(Coordonnees.etapeCourante)
        Coordonnees.etapeCourante = [[], [], []]
        # enregistre le nom et les paramètres de placement / rotation de chaque objet
        for i in FreeCAD.ActiveDocument.Objects:
            self.etapeCourante[0].append(i.Label)
            self.etapeCourante[1].append(i.Placement.Base)
            self.etapeCourante[2].append(i.Placement.Rotation.Q)
        self.etapeCourante.append(
            MouvementEnCours.getInstance().getListeNodesCourant())
        print(self.etapeCourante)

    def positionnerEtape(self, monEtape):
        for i in range(0, len(monEtape[0])):
            monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(
                monEtape[0][i])[0]  # on récupère l'objet
            # on le remet à ses coordonnées (x,y,z)
            monObjet.Placement.Base = monEtape[1][i]
            # on le repositionne avec son angle
            monObjet.Placement.Rotation.Q = monEtape[2][i]
        MouvementEnCours.getInstance().arreterLAnimation()
        for mouvement in monEtape[3]:
            MouvementEnCours.getInstance().ajouterNode(mouvement)

    def etapePrecedente(self):
        if(not (Coordonnees.pilePrecedente.estVide())):
            Coordonnees.pileSuivante.empiler(Coordonnees.etapeCourante)
            etape = Coordonnees.pilePrecedente.depiler()
            Coordonnees.etapeCourante = etape
            print(etape)
            Coordonnees.getInstance().positionnerEtape(etape)

    def etapeSuivante(self):
        if(not (Coordonnees.pileSuivante.estVide())):
            Coordonnees.pilePrecedente.empiler(Coordonnees.etapeCourante)
            etape = Coordonnees.pileSuivante.depiler()
            Coordonnees.etapeCourante = etape
            Coordonnees.getInstance().positionnerEtape(etape)
