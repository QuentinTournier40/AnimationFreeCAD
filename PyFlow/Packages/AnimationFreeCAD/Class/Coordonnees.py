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
        Coordonnees.estArriere = False

    def getInstance():
        if Coordonnees.__instance is None:
            Coordonnees.__instance = Coordonnees()
        return Coordonnees.__instance

    def ajouterEtape(self):
        Coordonnees.pilePrecedente.empiler(self.etape())
        if(Coordonnees.estArriere):
            Coordonnees.etapeSuivante = Pile()
        Coordonnees.estArriere = False
        
    def etape(self):
        etapeCourante = [[],[],[]]
        for i in FreeCAD.ActiveDocument.Objects:        #enregistre le nom et les paramètres de placement / rotation de chaque objet
            etapeCourante[0].append(i.Label)
            etapeCourante[1].append(i.Placement.Base)
            etapeCourante[2].append(i.Placement.Rotation.Q)
        etapeCourante.append(MouvementEnCours.getInstance().getListeNodesCourant())
        return etapeCourante

    def positionnerEtape(self, monEtape):
        for i in range(0,len(monEtape[0])):
                monObjet = FreeCAD.ActiveDocument.getObjectsByLabel(monEtape[0][i])[0]  #on récupère l'objet
                monObjet.Placement.Base = monEtape[1][i]        #on le remet à ses coordonnées (x,y,z)
                monObjet.Placement.Rotation.Q = monEtape[2][i]        #on le repositionne avec son angle
        
    def etapePrecedente(self):
        if(not (Coordonnees.pilePrecedente.estVide())):
            Coordonnees.pileSuivante.empiler(self.etape())
            etape = Coordonnees.pilePrecedente.depiler()
            Coordonnees.getInstance().positionnerEtape(etape)
            print("Etape précédente")
            Coordonnees.estArriere = True

    def etapeSuivante(self):
        if(not (Coordonnees.pileSuivante.estVide())):
            Coordonnees.pilePrecedente.empiler(self.etape())
            etape  = Coordonnees.pileSuivante.depiler()
            Coordonnees.getInstance().positionnerEtape(etape)
            print("Etape suivante")

    def positionnerDebut(self):
        while(not Coordonnees.pilePrecedente.estVide()):
            etape = Coordonnees.pilePrecedente.depiler()
            Coordonnees.pileSuivante.empiler(etape)
        etape = Coordonnees.pileSuivante.lireSommet()
        self.positionnerEtape(etape)