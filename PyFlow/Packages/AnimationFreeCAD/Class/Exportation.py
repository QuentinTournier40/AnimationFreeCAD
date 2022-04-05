
from asyncio.windows_events import NULL
from PyFlow.Packages.AnimationFreeCAD.Class.Mouvement import MainWindow
from pickle import FALSE, TRUE
import numpy as np
import os
import cv2
import glob
import FreeCADGui
from PySide import QtGui, QtCore
from Qt.QtWidgets import *


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

    def getFolderVideo(self):
        folder = QtGui.QFileDialog.getExistingDirectory()
        if folder == '':
            Exportation.getInstance().getFolderVideo()
        else:
            return folder

    def getNameVideo(self):
        name = QtGui.QInputDialog.getText(None, "Exportation de l'animation","Entrer le nom de la vidéo:")
        if name[0] == '':
            Exportation.getInstance().getNameVideo()
        else:
            return name
        
    def getDureeVideo(self):
        duree = QtGui.QInputDialog.getText(None, "Exportation de l'animation","Entrer la durée de la vidéo (en secondes):")
        if duree[0] == '':
            Exportation.getInstance().getDureeVideo()
        else:
            return duree

    def getNbrImages(self,duree,fps):
        nbrImages = int(duree) * fps
        return nbrImages

    def lancer(self): 
        preparation = True
        folder = Exportation.getInstance().getFolderVideo()
        name = Exportation.getInstance().getNameVideo()
        duree = Exportation.getInstance().getDureeVideo()


        while preparation == False:
            #Si toutes les informations sont bonnes, autorise l'exportation
            if folder is not NULL and name is not NULL and duree is not NULL:
                preparation = True
            else:
                preparation = False
            
        
        print("Démarrage de l'exportation | Nom "+str(name) +".avi | Emplacement "+str(folder))
 
        fps = 27 #Nombre d'image(s) par seconde(s)
        fond = "current" # current, black, white, Transparent 
        resolutionX = 1920
        resolutionY = 1080
        nbrImages = Exportation.getInstance().getNbrImages(duree[0],fps)


        #Création d'un dossier temporaires
        if not os.path.exists('../../../../exportation'):
            os.makedirs('../../../../exportation')


        for i in range(0,nbrImages):
            FreeCADGui.updateGui()
            FreeCADGui.ActiveDocument.ActiveView.saveImage("../../../../exportation/"+str(i)+"_screenshot.jpg",resolutionX, resolutionY,fond)
            print("Exportation en cours à "+str(int((i*100)/nbrImages))+" %")
        
        img_array = []
        print("Finalisation de l'exportation")
        for i in range(0,nbrImages):
            filename = '../../../../exportation/' + str(i) + '_screenshot.jpg'
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width,height)
            img_array.append(img)

        #Injection des paramétres vidéo
        out = cv2.VideoWriter(os.path.join(str(folder), str(name[0])+".avi"),cv2.VideoWriter_fourcc(*'DIVX'),fps, size)
        
        #Ecriture des images dans la vidéo
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()
        
        #Suppression des images
        for f in glob.glob('../../../../exportation/*.jpg'):
            os.remove(f)
            
        print("Exportation réussite")
    

