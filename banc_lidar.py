"""
GRO120: Banc de test lidar 
        Permet de tester le filtrage d'échantillons de données lidar.
                
        LES 4 ÉTAPES DE TRAITEMENT ATTENDUES SONT : 
           1. Lire les données d'un fichier texte (entrée)
           2. Filtrer les données lues (selon choix de l'utilisateur)
           3. Écrire les données filtrées dans un fichier texte (sortie)
           4. Afficher les valeurs statistiques des données filtrées valides (>=0)

Auteurs: Guillaume Larouche et Simon Côté 
Date: 24/09/2025
""" 

import sys
import filtrage
 

def lire():
    """
    DESC: Cette fonction permet de lire un document texte des données donné par le lidar.
        
          
    RETOUR: Tableau des données du document
    """
    nom="exemples/donnees_test.txt"
    point=[]
    
    doc = open(nom, "r")
    contenu = "a"
    while contenu !="":                     
        contenu = doc.readline()
        if contenu !="":
            p = float(contenu[0:len(contenu)-1])
        
            point.append(p)

    
    doc.close()
    
    
    return point
    

    

    

def decide_filtre():
    """
    DESC: Cette fonction demande à l'utilisateur quel filtre à appliquer aux données du lidar
          
    RETOUR: le numéro du choix de l'utilisateur
    """
    bonChoix= False
    while bonChoix==False:                                  #continue jusqu'à ce que l'entrée de l'utilisateur soit du bon format
        choix = input("Quel filtre vouler vous?\n" \
        "Écrire 1 pour faire un filtre de moyenne.\n" \
        "Écrire 2 pour un filtre médiane.\n"
        "Écrire 3 pour un filtre min et max\n"\
        "Écrire 4 pour arrêter le programme\n")
        if choix == '1' or choix=='2' or choix == '3' or choix =='4':
            bonChoix = True
        else :
            print("choix mal écrit")

    return choix

def ecrire(points):
    """
    DESC: Cette fonction prend les données filtrés et les écrit dans une bnouveau document vierge
          
    """
    doc = open("exemples/donnees_final", 'w')
    for p in points:
        doc.write(str(p)+"\n")
    doc.close()
    


#===========================================
if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme
    """
    print("Test lidar (GRO120)")
    continu = True
    points=lire()
    while continu == True:
        choix =decide_filtre()
        if choix == '1':
            points = filtrage.filtre_moyenne(points)
        elif choix=='2':
            points = filtrage.filtre_mediane(points)
        elif choix =='3':
            points=filtrage.filtre_min_max(points)
        else:
            continu = False
            tmp = filtrage.filtre_bonne_valeur(points)
            total = 0
            for p in tmp:
                total = total+p
            print("moyenne:", round(total/len(tmp),1))
            print("Bonne valeur:", len(tmp))
            print("valeur total:", len(points))
            ecrire(points)
                

        

    
    