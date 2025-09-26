"""
GRO120: Tests unitaires pour le module filtrage

Auteur: Francois Ferland
Date: 18/09/2025

Modifié par: Guillaume Larouche et Simon Côté
Date: 24/09/2025
""" 

import filtrage

#===========================================
def test_filtre_min_max():
    """
    DESC: Test la fonction filtre_min_max. Nous avertie si la fonction ne fonctionne pas
    
    NOTE: On fournit un tableau de donnees, qui retourne un tableau filtré 
          selon les valeurs minimum et maximum spécifiées 
    """
    
    
    
    donnees = [1,50,0,-10]
    reponse = [1,10,-1,-1]    
    test = filtrage.filtre_min_max(donnees, 1, 10)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [3,3.567667676767,15,0.5,15]                                  
    reponse=[3,3.567667676767,15,0.5,15]
    test=filtrage.filtre_min_max(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [3]                                  
    reponse=[3]
    test=filtrage.filtre_min_max(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"
    
    donnees = []                                  
    reponse=[]
    test=filtrage.filtre_min_max(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"
    
    pass

def test_filtre_moyenne():
    """
    DESC: Test la fonction filtre_moyenne. Nous avertie si la fonction ne fonctionne pas
    
    NOTE: On fournit un tableau de donnees, qui retourne un tableau filtré 
          selon les valeurs moyenne
    """

    donnees = [1,-1]
    reponse=[0,0]
    test = filtrage.filtre_moyenne(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}" 

    donnees = [3,3.5,6,9,7.2]                                              
    reponse=[3.2,4.2,6.2,7.4,8.1]
    test = filtrage.filtre_moyenne(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"
    
    donnees = [1]
    reponse=[1]
    test = filtrage.filtre_moyenne(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}" 

    donnees = [-1,-1,-5,-1,-5, -4]
    reponse=[-1,-2.3,-2.3,-3.7,-3.3,-4.5]
    test = filtrage.filtre_moyenne(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}" 

    donnees = [-1,1,-5,-1,5, 4]
    reponse=[0,-1.7,-1.7,-0.3,2.7,4.5]
    test = filtrage.filtre_moyenne(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}" 

    donnees = []                                  
    reponse=[]
    test=filtrage.filtre_moyenne(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [-1,-1,-5.927379272734,-1,-5, -4]
    reponse=[-1,-2.6,-2.6,-4,-3.3,-4.5]
    test = filtrage.filtre_moyenne(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}" 

    pass

def test_filtre_mediane():
    """
    DESC: Test la fonction filtre_mediane. Nous avertie si la fonction ne fonctionne pas
    
    NOTE: On fournit un tableau de donnees, qui retourne un tableau filtré 
          selon les valeurs médiane
    """

    donnees = [1,-1]       
    reponse=[1,-1]      
    test = filtrage.filtre_mediane(donnees)                                #deux tests différents
    assert test == reponse, f"Erreur: {test} != {reponse}"

    donnees = [3,3.5,6,9,7.2898998889]
    reponse=[3,3.5,6,7.2898998889,7.2898998889]
    test = filtrage.filtre_mediane(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"
    
    donnees = [3]                                  
    reponse=[3]
    test=filtrage.filtre_mediane(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"
    
    donnees = []                                  
    reponse=[]
    test=filtrage.filtre_mediane(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}"
    pass

    donnees = [-1,-1,-5,-1,-5, -4]
    reponse=[-1,-1,-1,-5,-4,-4]
    test = filtrage.filtre_mediane(donnees)
    assert test == reponse, f"Erreur: {test} != {reponse}" 



def alltest():
    """
    DESC: Cette fonction permet de faire tous les tests de toutes les fonctions
    
    """
    test_filtre_min_max()
    test_filtre_moyenne()
    test_filtre_mediane()
    
    
    print("Tous les tests ont réussi.")







if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme qui exécute tout les tests des filtres
    """ 
    test_filtre_min_max()
    test_filtre_moyenne()
    test_filtre_mediane()
     
    print("Tous les tests ont réussi.")
    