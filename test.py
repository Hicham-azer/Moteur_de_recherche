from lib2to3.pygram import pattern_grammar
from turtle import bgcolor
from unittest import skip
import cv2
import os
import numpy as np

#convertir l'image en matrice ( niveau de gris )
def img_to_mat(image_path) :
    img=cv2.imread(image_path)
    img= cv2.cvtColor(img ,cv2.COLOR_BGR2GRAY)
    img=cv2.resize(img ,(128,128))
    mat=img.astype('float32')
    return mat

#matrice de cooccurence
def mat_to_comat(mat) :
    comat = np.zeros((256,256))
    for i in range (0 , 128) :
        for j in range (0 ,128):
            if i == 127 or j == 127 :
                skip
            elif mat[i][j] == mat[i+1][j+1]:
                comat[int(mat[i][j])][int(mat[i+1][j+1])] += 1
    return comat

#calculer l'uniformité
def descripteur_texture(comat):
    uniformite = 0
    for i in range ( 0 , 256) :
        for j in range ( 0 , 256) :
            uniformite += comat[i][j]**2
    return uniformite

#calculer la distance euclidienne
def distance_euclidienne(uniformite1,uniformite2) :
    return abs(uniformite1-uniformite2)


#indexer la dataset 
#utliser le chemin de votre dataset (r"dataset_path")
def index() :
    dictionary_uniformite={}
    for image in os.listdir(r"C:\Users\hicha\Desktop\moteur_de_recherche\dataset") :
        mat = img_to_mat(r"C:\Users\hicha\Desktop\moteur_de_recherche\dataset" + "\\" + image)
        comat = mat_to_comat(mat)
        uniformite = descripteur_texture(comat)
        dictionary_uniformite[image]=int(uniformite)
        list = sorted(dictionary_uniformite.items() ,key=lambda x: x[1])
        fichier_data = open(r"C:\Users\hicha\Desktop\moteur_de_recherche\dataindexed.txt", "w")
        for tuple in list :
            fichier_data.write(tuple[0] + "\n")
            fichier_data.write(str(tuple[1]) + "\n")
        fichier_data.close
    return fichier_data

#Lire le fichier de la data indexé ... il faut préciser le path du fichier
def lire_dataindexed() :
    fichier_data = open(r"C:\Users\hicha\Desktop\moteur_de_recherche\dataindexed.txt", "r")
    lignes = []
    dictionary = {}
    for ligne in fichier_data :
        ligne = ligne.strip()
        lignes.append(ligne)
    for i in range(0 ,len(lignes)-1 , 2) :
        dictionary[lignes[i]] = int(lignes[i+1])
    fichier_data.close
    return dictionary

def resultat(path_image , nbr_resultat ):
    list = []
    resultat = []
    mat = img_to_mat(path_image)
    comat = mat_to_comat(mat)
    uniformite = descripteur_texture(comat)
    dictionary = lire_dataindexed()
    for key , value in dictionary.items() :
        dictionary[key]=distance_euclidienne(uniformite,value )
        list.append(distance_euclidienne(uniformite , value))
    list.sort()
    list = list [:nbr_resultat]
    print (list)
    for key , value in dictionary.items() : 
        if value in list :
            print (value)
            resultat.append(key)
    return resultat

#Affichage des resultats dans une fenetre
def affichage_resultats(resultats , path_query) :
    query = cv2.imread(path_query)
    cv2.imshow( "source" , query )
    cv2.waitKey(0)
    for path in resultats :
        img =cv2.imread(r"C:\Users\hicha\Desktop\moteur_de_recherche\dataset" + "\\" + path)
        cv2.imshow( "resultat" , img )
        cv2.waitKey(0)
    return 0





path_query = r"C:\Users\hicha\Desktop\moteur_de_recherche\dataset\0001.png"
resultats = resultat(path_query ,4)
affichage_resultats(resultats , path_query)