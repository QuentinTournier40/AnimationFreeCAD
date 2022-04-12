
from asyncio.windows_events import NULL
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import MainWindow
from pickle import FALSE, TRUE
import numpy as np
import os
import cv2
import glob
import FreeCADGui
from PySide import QtGui, QtCore
from PySide2.QtWidgets import *


class Exportation():
    __instance = None

    def __init__(self):
        if Exportation.__instance is not None :
            raise Exception("Utiliser la méthode get_instance() pour obtenir une instance de l'exportation")

    def getInstance():
        if Exportation.__instance is None:
            print("")
            Exportation.__instance = Exportation()
        else:
            print("")

        return Exportation.__instance


    def lancer(self):
        #Récupération des informations
        folder = QtGui.QFileDialog.getExistingDirectory()
        if folder == '':
            FenetreErreurExportation("Aucun dossier sélectionné !")
        else:
            nameVideo = QtGui.QInputDialog.getText(None, "Exportation de l'animation","Entrer le nom de la vidéo:")
            name = nameVideo[0]
            name = ''.join(filter(str.isalnum, name))
            if name == '':
                FenetreErreurExportation("Nom de la vidéo incorrecte !")
            else:
                duree = QtGui.QInputDialog.getInt(None, "Exportation de l'animation","Entrer la durée de la vidéo (en secondes):",1,1)
                temps = duree[0]
                if temps <= 0:
                    FenetreErreurExportation("Valeur incorrecte !")
                else:
                    ListeFormat = ("mp4", "avi")
                    format= QtGui.QInputDialog.getItem(None, "Exportation de l'animation","Listes des formats vidéo disponibles",ListeFormat)

                    ListeFond = ("current", "black", "white", "Transparent")
                    fond= QtGui.QInputDialog.getItem(None, "Exportation de l'animation","Listes des arrières plan disponible",ListeFond)

                    print("[Exportation] Démarrage")

                    fps = 27 #Nombre d'image(s) par seconde(s)
                    resolutionX = 1920
                    resolutionY = 1080
                    nbrImages = int(duree[0]) * fps

                    #Création d'un dossier temporaires
                    if not os.path.exists('../../../../ExportationFreeCAD'):
                        os.makedirs('../../../../ExportationFreeCAD')

                    cpt = 0
                    for i in range(0,nbrImages):
                        FreeCADGui.updateGui()
                        FreeCADGui.ActiveDocument.ActiveView.saveImage("../../../../ExportationFreeCAD/"+str(i)+"_screenshot.jpg",resolutionX, resolutionY,fond[0])
                        cpt += 1
                        if cpt == 5:
                            print("[Exportation] "+str(int((i*100)/nbrImages))+" %")
                            cpt = 0

                    print("[Exportation] Finalisation")
                    img_array = []
                    for i in range(0,nbrImages):
                        filename = '../../../../ExportationFreeCAD/' + str(i) + '_screenshot.jpg'
                        img = cv2.imread(filename)
                        height, width, layers = img.shape
                        size = (width,height)
                        img_array.append(img)

                    #Injection des paramétres vidéo
                    out = cv2.VideoWriter(os.path.join(str(folder), str(name)+"."+str(format[0])),cv2.VideoWriter_fourcc(*'DIVX'),fps, size)

                    #Ecriture des images dans la vidéo
                    for i in range(len(img_array)):
                        out.write(img_array[i])
                    out.release()

                    #Suppression des images
                    for f in glob.glob('../../../../ExportationFreeCAD/*.jpg'):
                        os.remove(f)

                    print("[Exportation] Terminer -> "+str(folder)+"/"+str(name)+"."+str(format[0]))


class FenetreErreurExportation():
    def __init__(self,message):
        fenetre = MainWindow()
        msg = QMessageBox(fenetre)
        msg.setWindowTitle("Exportation Impossible")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setText(message)
        x = msg.exec_()


