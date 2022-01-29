from PySide import QtCore
import functools
import FreeCAD

class Rotation():

    def __init__(self, unNode, unObjet, unAxeDeRotation, unCentreDeRotation, unAngleDeDebut, unAngleDeFin, uneDuree, estBoucle, estAllerRetour):
        self.node = unNode
        self.objet = unObjet
        self.axeDeRotation = unAxeDeRotation
        self.centreDeRotation = unCentreDeRotation
        self.angleDeDebut = unAngleDeDebut
        self.angleDeFin = unAngleDeFin
        self.duree = uneDuree
        self.angleARepeter = (self.angleDeFin - self.angleDeDebut) / (32*self.duree)
        self.estBoucle = estBoucle
        self.estAllerRetour = estAllerRetour
        self.premierePartieAllerRetour = True
        self.etape = 0
    
    def repetitionMouvement(self, unTimer):
        if(self.etape != (32*self.duree)):
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, self.angleARepeter)
            self.etape += 1
        else:
            unTimer.stop()
            self.etape = 0
            self.node["outExec"].call()

    def repetitionMouvementSansFin(self, unTimer):
        self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, self.angleARepeter)

    def repetitionMouvementAllerRetour(self, unTimer):
        if(self.etape < (32*self.duree) and self.premierePartieAllerRetour):
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, self.angleARepeter)
            self.etape += 1
        elif(self.etape == (32*self.duree) and self.premierePartieAllerRetour):
            self.premierePartieAllerRetour = False
        elif(self.etape > 0 and not(self.premierePartieAllerRetour)):
            self.etape -= 1
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, -self.angleARepeter)
        elif(self.etape == 0 and not(self.premierePartieAllerRetour)):
            unTimer.stop()
            self.premierePartieAllerRetour = True
            self.node["outExec"].call()

    def repetitionMouvementSansFinEtAllerRetour(self, unTimer):
        if(self.etape < (32*self.duree) and self.premierePartieAllerRetour):
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, self.angleARepeter)
            self.etape += 1
        elif(self.etape == (32*self.duree) and self.premierePartieAllerRetour):
            self.premierePartieAllerRetour = False
        elif(self.etape > 0 and not(self.premierePartieAllerRetour)):
            self.etape -= 1
            self.objet.Placement.rotate(self.centreDeRotation, self.axeDeRotation, -self.angleARepeter)
        elif(self.etape == 0 and not(self.premierePartieAllerRetour)):
            self.premierePartieAllerRetour = True
    
    def rotation(self):
        self.objet.Placement.Rotation = FreeCAD.Rotation(self.axeDeRotation, self.angleARepeter)
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