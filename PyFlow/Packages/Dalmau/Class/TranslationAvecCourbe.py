import FreeCAD
from PySide import QtCore
import functools

class TranslationAvecCourbe():
    
    def __init__(self, unNode, unObjet, uneCourbe, uneDuree, estBoucle, estAllerRetour):
        self.node = unNode
        self.objet = unObjet
        self.courbe = uneCourbe
        self.duree = uneDuree
        self.estBoucle = estBoucle
        self.estAllerRetour = estAllerRetour
        self.etape = 0
        self.premierePartieAllerRetour = True
        self.pointsTrajectoire = self.creerListeDePointsAvecUneCourbe(self.courbe)

    def creerListeDePointsAvecUneCourbe(self, uneCourbe):
        return uneCourbe.Shape.discretize(32*self.duree)

    def repetitionMouvement(self, unTimer):
        if(self.etape != len(self.pointsTrajectoire)):
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
            self.etape += 1
        else:
            unTimer.stop()
            self.etape = 0
            self.node["outExec"].call()

    def repetitionMouvementSansFin(self, unTimer):
        if(self.etape != len(self.pointsTrajectoire)):
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
            self.etape += 1
        else:
            self.etape = 0

    def repetitionMouvementAllerRetour(self, unTimer):
        if(self.etape != len(self.pointsTrajectoire) and self.premierePartieAllerRetour):
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
            self.etape += 1
        elif(self.etape == len(self.pointsTrajectoire) and self.premierePartieAllerRetour):
            self.premierePartieAllerRetour = False
        elif(self.etape > 0 and not(self.premierePartieAllerRetour)):
            self.etape -= 1
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
        elif(self.etape == 0 and not(self.premierePartieAllerRetour)):
            unTimer.stop()
            self.premierePartieAllerRetour = True
            self.node["outExec"].call()
        
    def repetitionMouvementSansFinEtAllerRetour(self, unTimer):
        if(self.etape != len(self.pointsTrajectoire) and self.premierePartieAllerRetour):
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
            self.etape += 1
        elif(self.etape == len(self.pointsTrajectoire) and self.premierePartieAllerRetour):
            self.premierePartieAllerRetour = False
        elif(self.etape > 0 and not(self.premierePartieAllerRetour)):
            self.etape -= 1
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
        elif(self.etape == 0 and not(self.premierePartieAllerRetour)):
            self.premierePartieAllerRetour = True

    def translater(self):
        timer = QtCore.QTimer()
        if(self.estBoucle and self.estAllerRetour):
            repetitionMouvement = functools.partial(self.repetitionMouvementSansFinEtAllerRetour, unTimer = timer)
        elif(self.estBoucle and not(self.estAllerRetour)):
            repetitionMouvement = functools.partial(self.repetitionMouvementSansFin, unTimer = timer)
        elif(self.estAllerRetour and not(self.estBoucle)):
            repetitionMouvement = functools.partial(self.repetitionMouvementAllerRetour, unTimer = timer)
        else:
            repetitionMouvement = functools.partial(self.repetitionMouvement, unTimer = timer)
        timer.timeout.connect(repetitionMouvement)
        timer.start(20)