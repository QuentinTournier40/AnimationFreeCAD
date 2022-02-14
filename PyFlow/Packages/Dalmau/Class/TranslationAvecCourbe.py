import FreeCAD
from PyFlow.Packages.Dalmau.Class.Mouvement import NOMBRE_D_OR, Mouvement
from PySide import QtCore
import functools
import time

class TranslationAvecCourbe(Mouvement):
    
    def __init__(self, unNode):
        super().__init__(unNode)
        self.courbe = FreeCAD.ActiveDocument.getObjectsByLabel(unNode.courbe.getData())[0]
        self.nbrPoints = round(NOMBRE_D_OR * self.duree)
        self.pointsTrajectoire = self.creerListeDePointsAvecUneCourbe(self.courbe)

    def creerListeDePointsAvecUneCourbe(self, uneCourbe):
        return uneCourbe.Shape.discretize(self.nbrPoints)

    def repetitionMouvement(self):
        if(self.etape != self.nbrPoints):
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
            self.etape += 1
        else:
            self.timer.stop()
            print(time.time() - self.monTemps)
            self.etape = 0
            self.sortieNode.call()

    def repetitionMouvementSansFin(self):
        if(self.etape != self.nbrPoints):
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
            self.etape += 1
        else:
            self.etape = 0

    def repetitionMouvementAllerRetour(self):
        if(self.etape != self.nbrPoints and self.premiereEtapeAllerRetour):
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
            self.etape += 1
        elif(self.etape == self.nbrPoints and self.premiereEtapeAllerRetour):
            self.premiereEtapeAllerRetour = False
        elif(self.etape > 0 and not(self.premiereEtapeAllerRetour)):
            self.etape -= 1
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
        elif(self.etape == 0 and not(self.premiereEtapeAllerRetour)):
            self.timer.stop()
            self.premiereEtapeAllerRetour = True
            self.sortieNode.call()
        
    def repetitionMouvementSansFinEtAllerRetour(self):
        if(self.etape != self.nbrPoints and self.premiereEtapeAllerRetour):
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
            self.etape += 1
        elif(self.etape == self.nbrPoints and self.premiereEtapeAllerRetour):
            self.premiereEtapeAllerRetour = False
        elif(self.etape > 0 and not(self.premiereEtapeAllerRetour)):
            self.etape -= 1
            self.objet.Placement.Base = (self.pointsTrajectoire[self.etape])
        elif(self.etape == 0 and not(self.premiereEtapeAllerRetour)):
            self.premiereEtapeAllerRetour = True

    def translater(self):
        if(self.estBoucle and self.estAllerRetour):
            repetitionMouvement = functools.partial(self.repetitionMouvementSansFinEtAllerRetour)
        elif(self.estBoucle and not(self.estAllerRetour)):
            repetitionMouvement = functools.partial(self.repetitionMouvementSansFin)
        elif(self.estAllerRetour and not(self.estBoucle)):
            repetitionMouvement = functools.partial(self.repetitionMouvementAllerRetour)
        else:
            repetitionMouvement = functools.partial(self.repetitionMouvement)
        self.timer.timeout.connect(repetitionMouvement)
        self.timer.start()
        self.monTemps = time.time()