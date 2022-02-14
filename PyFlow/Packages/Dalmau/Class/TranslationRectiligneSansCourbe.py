from PyFlow.Packages.Dalmau.Class.TranslationAvecCourbe import TranslationAvecCourbe
import FreeCAD
import Draft

class TranslationRectiligneSansCourbe(TranslationAvecCourbe):

    def __init__(self, unNode):
        uneLigne = self.creerLigneAvecDeuxPoints(unNode.pointDepart.getData(), unNode.pointDeFin.getData())
        unNode.courbe = uneLigne
        super().__init__(unNode)
        self.supprimerCourbe(uneLigne)

    def creerLigneAvecDeuxPoints(self, point1, point2):
        placement = FreeCAD.Placement()
        placement.Rotation.Q = (0,0,0,1)
        placement.Base = point1
        points = [point1, point2]
        line = Draft.makeWire(points, placement=placement, closed=False, face=False, support=None)
        FreeCAD.ActiveDocument.recompute()
        return line

    def supprimerCourbe(self, courbe):
        FreeCAD.ActiveDocument.removeObject(courbe.Label)