from PyFlow.Packages.AnimationFreeCAD.Nodes.en.NodeAnimation import NodeAnimation
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import *
import functools
from PySide import QtCore
import math
from math import *


import FreeCAD

class SpinXNode(NodeAnimation):
    def __init__(self, name):
        super(SpinXNode, self).__init__(name)
        self.createInputPin("Angle", "FloatPin")
        self.duree = self.createInputPin("Duration", "FloatPin")

    def compute(self, *args, **kwargs):  
        if(self.getData("Object") == DEFAULT_VALUE_OBJECT_PIN):
            return FenetreErreur("Error", self.name, self.objet.name, "Please choose an object.")  
        if(self.getData("Duration") <= 0):
            return FenetreErreur("Error", self.name, self.duree.name, "Duration cannot be less than or equal to 0.")

        self.objet = FreeCAD.ActiveDocument.getObjectsByLabel(self.getData("Object"))[0]
        self.angle = self.getData("Angle")
        self.duree = self.getData("Duration")

        super().compute()        
              
        self.nbrAngle = round(NOMBRE_D_OR * self.duree)
        self.angleParEtape = self.angle/self.nbrAngle
       
        self.compteur = 0

        self.timer = QtCore.QTimer()
        self.timer.setInterval(20)

        mouvement = functools.partial(self.mouvementRotationX)

        self.timer.timeout.connect(mouvement)
        self.timer.start()

        self.setData("Final position", self.objet.Placement.Base)
        self.setData("Object use", self.objet.Label)

    def mouvementRotationX(self):
      if(self.compteur >= self.nbrAngle):
          self.timer.stop()
      m = self.objet.Placement.Rotation.Matrix
      m.rotateX(math.radians(self.angleParEtape))
      q = self.matrixToQ(m)
      self.objet.Placement.Rotation = q
      self.compteur += 1

    @staticmethod
    def category():
        return 'en|Spin|Duration'

    @staticmethod
    def description():
        return "Rotates objects around the x axis."
        
    def getTrace(self, m):
        trace = m.A11 + m.A22 + m.A33 + 1
        return trace

    def matrixToQ(self, m):
        """https://jeux.developpez.com/faq/math/?page=quaternions"""
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