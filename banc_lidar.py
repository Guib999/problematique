"""
GRO120: Banc de test lidar 
        Permet de tester le filtrage d'échantillons de données lidar.
                
        LES 4 ÉTAPES DE TRAITEMENT ATTENDUES SONT : 
           1. Lire les données d'un fichier texte (entrée)
           2. Filtrer les données lues (selon choix)
           3. Écrire les données filtrées dans un fichier texte (sortie)
           4. Afficher les valeurs statistiques des données filtrées valides (>=0)

Auteurs: ...
Date: jj/mm/aaaa
""" 

import sys

from os import *

#===========================================
# Méthode(s) à compléter...
#===========================================

def lire():
    #print(getcwd())
    nom="exemples/donnees_test.txt"
    point=[]
    try:
        doc = open(nom, "r")
        contenu = "a"
        while contenu !="":
            contenu = int(doc.readline())
            point.append(contenu)

        
        doc.close()
    except Exception as e:
        print("erreur: ", e)
    
    return point
    

    

    

def decide_filtre():
    choix = input("Quel filtre vouler vous?\n" \
    "Écrire 1 pour faire un filtre de moyenne.\n" \
    "Écrire 2 pour un filtre médiane.\n",)

    return choix



#===========================================
if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme
    """
    print("Test lidar (GRO120)")
    #decide_filtre()
    lire()
    