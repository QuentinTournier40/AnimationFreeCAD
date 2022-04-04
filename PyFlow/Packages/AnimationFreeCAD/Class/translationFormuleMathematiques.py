from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import Mouvement
from PySide import QtCore
import functools
import FreeCAD
import time
from PyFlow.Packages.AnimationFreeCAD.Class.MouvementEnCours import MouvementEnCours

class translationFormuleMathematiques(Mouvement):
    def __init__(self, equationX, equationY, equationZ, unNode):
        Mouvement.__init__(self, unNode)
        self.equationX = equationX
        self.equationY = equationY
        self.equationZ = equationZ
        self.pas = 0.0319
        self.t = 0

    def calculTrajectoire(self, estAllerRetour, duree):
        if(estAllerRetour):
            duree = duree
            self.pas = self.pas * 2
        self.duree = duree
        self.nbrPoints = round(self.duree / self.pas)

    def calculPoints(self):
        posX = eval(self.equationX)
        posY = eval(self.equationY)
        posZ = eval(self.equationZ)
        return FreeCAD.Vector(posX, posY, posZ)

    def mouvement(self, sens, suite):
        placementObjet = self.calculPoints()
        self.objet.Placement.Base = placementObjet
        if(sens):
            self.t += self.pas
            self.etape += 1
        else:
            self.t -= self.pas
            self.etape -= 1

        if(sens):
            if(self.t >= self.duree):
                self.timer.stop()
                MouvementEnCours.getInstance().enleverNode(self)
                if(suite == ""):
                    self.sortieNode.call()
                else:
                    exec(suite)
        else:
            if(self.t <= 0):
                self.timer.stop()
                MouvementEnCours.getInstance().enleverNode(self)
                if(suite == ""):
                    self.sortieNode.call()
                else:
                    exec(suite)

    def execution(self, sens, paramSuite, etape=-1):
        if(etape == -1):
            if(sens):
                self.etape = 0
                self.t = 0
            else:
                self.etape = self.nbrPoints - 1
                self.t = self.duree
        else:
            self.allerALEtape(etape)

        mouvement = functools.partial(self.mouvement, sens=sens, suite=paramSuite)
        # Bug de timer lorsque le mouvement est un aller boucle, il se mets à avancer de plus en vite
        # Test : Lorsqu'on fait 2 aller à la suite le 2ème est accéléré, pourquoi ?
        MouvementEnCours.getInstance().ajouterNode(self)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)

        self.timer.timeout.connect(mouvement)
        self.timer.start()

        self.temps = time.time()

    def allerALEtape(self, etape):
        self.t = self.pas * etape
        self.etape = etape
        placementObjet = self.calculPoints()
        self.objet.Placement.Base = placementObjet
