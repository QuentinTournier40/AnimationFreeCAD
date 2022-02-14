from PyFlow.Packages.Dalmau.Class.Mouvement import NOMBRE_D_OR, Mouvement
from PySide import QtCore
import functools
import FreeCAD

class Rotation(Mouvement):

    def __init__(self, unNode):
        super().__init__(unNode)
        self.axeDeRotation = unNode.axeRotation.getData()
        self.centreDeRotation = unNode.centreRotation.getData()
        self.angleDeDebut = unNode.angleDebut.getData()
        self.angleDeFin = unNode.angleFin.getData()
        self.nbrPoints = round(NOMBRE_D_OR * self.duree)
        self.angleARepeter = (self.angleDeFin - self.angleDeDebut) / self.nbrPoints

    def repetitionMouvement(self):
        if(self.etape != self.nbrPoints):
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, self.angleARepeter)
            self.etape += 1
        else:
            self.timer.stop()
            self.etape = 0
            self.sortieNode.call()

    def repetitionMouvementSansFin(self):
        self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, self.angleARepeter)

    def repetitionMouvementAllerRetour(self):
        if(self.etape < self.nbrPoints and self.premierePartieAllerRetour):
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, self.angleARepeter)
            self.etape += 1
        elif(self.etape == self.nbrPoints and self.premierePartieAllerRetour):
            self.premierePartieAllerRetour = False
        elif(self.etape > 0 and not(self.premierePartieAllerRetour)):
            self.etape -= 1
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, -self.angleARepeter)
        elif(self.etape == 0 and not(self.premierePartieAllerRetour)):
            self.timer.stop()
            self.premierePartieAllerRetour = True
            self.sortieNode.call()

    def repetitionMouvementSansFinEtAllerRetour(self):
        if(self.etape < self.nbrPoints and self.premierePartieAllerRetour):
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, self.angleARepeter)
            self.etape += 1
        elif(self.etape == self.nbrPoints and self.premierePartieAllerRetour):
            self.premierePartieAllerRetour = False
        elif(self.etape > 0 and not(self.premierePartieAllerRetour)):
            self.etape -= 1
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, -self.angleARepeter)
        elif(self.etape == 0 and not(self.premierePartieAllerRetour)):
            self.premierePartieAllerRetour = True
    
    def rotation(self):
        self.objet.Placement.Rotation = FreeCAD.Rotation(self.axeDeRotation, self.angleARepeter)
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