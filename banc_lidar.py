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
import test_filtrage
 

def lire():
    """
    DESC: Cette fonction permet de lire un document texte des données donné par le lidar. Le nom du fichier est 
        demandé à l'utilisateur.
        
          
    RETOUR: Tableau des données du document
    """
    point=[]
    while(True):            #demande en continue à l'utilisateur un nom de fichier qui existe
        nom=input("Quel est le nom du fichier de donner?: \n")
        
        try:                        #on vérifie que le fichier existe sans fermer le programme
            doc = open("exemples/"+nom, "r")
            contenu = "a"
            while contenu !="":                     #lit toute les ligne du fichier
                contenu = doc.readline()
                if contenu !="":
                    p = float(contenu[0:len(contenu)-1])
                
                    point.append(p)
            doc.close()
            print()
            break
        except FileNotFoundError:
            print("Fichier introuvable")
            print()
    
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
        print()

    return choix

def ecrire(points):
    """
    DESC: Cette fonction prend les données filtrés et les écrit dans une nouveau document vierge. Demande à l'utilisateur 
        le nom du fichier.
          
    """
    nom = input("Quel est le nom du fichier de sortie? \n")
    doc = open("exemples/"+nom , 'w')
    for p in points:
        doc.write(str(p)+"\n")
    doc.close()
    print()
    



if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme. Démarre toute la logique du programme
    """
    test_filtrage.alltest()
    continu = True  
    points=lire()
    while continu == True:
        choix =decide_filtre()
        if choix == '1':                        #applique le filtre selon le choix de l'utilisateur
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
            ecrire(points)
            
            print("moyenne:", round(total/len(tmp),1))
            print("Bonne valeur:", len(tmp))
            print("valeur total:", len(points))
            
                

        

    
    