from PyFlow.Packages.AnimationFreeCAD.Nodes.fr.NodeAnimation import NodeAnimation
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
from Qt.QtWidgets import *
import functools
from PySide import QtCore
import math
from math import *


import FreeCAD

class RotationZNode(NodeAnimation):
    def __init__(self, name):
        super(RotationZNode, self).__init__(name)
        self.createInputPin("Angle", "FloatPin")
        self.duree = self.createInputPin("Duree", "FloatPin")

    def compute(self, *args, **kwargs):  
        if(self.getData("Objet") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Erreur", self.name, self.objet.name, "Veuillez choisir un objet à mouvoir.")  
        if(self.getData("Duree") <= 0):
            return FenetreErreur("Erreur", self.name, self.duree.name, "La durée ne peut pas être inférieure ou égale à 0.")

        self.objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Objet"))[0]
        self.angle = self.getData("Angle")        
        self.duree = self.getData("Duree")

        super().compute()        
              
        self.nbrAngle = round(NOMBRE_D_OR * self.duree)
        self.angleParEtape = self.angle/self.nbrAngle
       
        self.compteur = 0

        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)

        mouvement = functools.partial(self.mouvementRotationX)

        self.timer.timeout.connect(mouvement)
        self.timer.start()

        self.setData("Position finale", self.objet.Placement.Base)
        self.setData("Objet use", self.objet.Label)

    def mouvementRotationX(self):
      if(self.compteur >= self.nbrAngle):
          self.timer.stop()
      m = self.objet.Placement.Rotation.Matrix
      m.rotateZ(float(format(math.radians(self.angleParEtape), ".18f")))
      q = self.matrixToQ(m)
      self.objet.Placement.Rotation = q
      self.compteur += 1

    @staticmethod
    def category():
        return 'fr|Rotation|Durée'

    @staticmethod
    def description():
        return "Fait tourner des objets."
        
    def getTrace(self, m):
        trace = m.A11 + m.A22 + m.A33 + 1
        return trace

    def matrixToQ(self, m):
        trace = self.getTrace(m)
        if(trace > 0 ):
            s = 0.5/sqrt(trace)
            x = (m.A32 - m.A23) * s
            y = (m.A13 - m.A31) * s
            z = (m.A21 - m.A12) * s
            w = 0.25/s
        else:
            if(m.A11 >= m.A22 and m.A11 >= m.A33):
                s = sqrt(1 + m.A11 - m.A22 - m.A33) * 2
                x = 0.25 * s
                y = (m.A12 + m.A21)/s
                z = (m.A13 + m.A31)/s
                w = (m.A32 - m.A23)/s
            elif(m.A22 >= m.A11 and m.A22 >= m.A33):
                s = sqrt(1 - m.A11 + m.A22 - m.A33) * 2
                x = (m.A12 + m.A21)/s
                y = 0.25 * s
                z = (m.A23 + m.A32)/s
                w = (m.A13 - m.A31)/s
            elif(m.A33 >= m.A11 and m.A33 >= m.A22):
                s = sqrt(1 - m.A11 - m.A22 + m.A33) * 2
                x = (m.A13 + m.A31)/s
                y = (m.A23 + m.A32)/s
                z = 0.25 * s
                w = (m.A21 - m.A12)/s
        return (x,y,z,w)    