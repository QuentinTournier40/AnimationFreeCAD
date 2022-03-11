from PyFlow.Packages.Dalmau.Class.TranslationAvecCourbe import TranslationAvecCourbe

import FreeCAD
import Draft

class TranslationSansCourbe(TranslationAvecCourbe):
    def __init__(self, coordonnes, unNode):
        courbe = self.creerLigneAvecDeuxPoints(coordonnes[0],coordonnes[1])
        TranslationAvecCourbe.__init__(self, courbe,unNode)    
        
    def creerLigneAvecDeuxPoints(self, point1, point2):
        placement = FreeCAD.Placement()
        placement.Base = point1
        points = [point1, point2]
        line = Draft.makeWire(points, placement=placement, closed=False, face=False, support=None)
        Draft.autogroup(line)
        FreeCAD.ActiveDocument.recompute()
        FreeCAD.ActiveDocument.Line.Visibility = False
        return line

    def calculTrajectoire(self, estAllerRetour, uneDuree):
        super().calculTrajectoire(estAllerRetour, uneDuree)
        FreeCAD.ActiveDocument.removeObject(self.courbe.Label)