"""
GRO120: Tests unitaires pour le module filtrage

Auteur: Francois Ferland
Date: 18/09/2025

Modifié par: ...
Date: ...
""" 

import filtrage

#===========================================
def test_filtre_min_max():
    """
    DESC: Test la fonction filtre_min_max
    
    NOTE: On fournit un tableau de donnees, qui retourne un tableau filtré 
          selon les valeurs minimum et maximum spécifiées 
    """
    
    
    
    donnees = [1,50,0,-10]
    donnees2 = [3,3.5,15,0.5,15]
    reponse = [1,10,-1,-1]
    reponse2=[3,3.5,15,0.5,15]

    test = filtrage.filtre_min_max(donnees, 1, 10)
    test2=filtrage.filtre_min_max(donnees2)

    assert test == reponse, f"Erreur: {test} != {reponse}"
    assert test2 == reponse2, f"Erreur: {test2} != {reponse2}"
    
    
    pass

def test_filtre_moyenne():

    donnees = [1,-1]
    donnees2 = [3,3.5,6,9,7.2]
    reponse=[0,0]
    reponse2=[3.2,4.2,6.2,7.4,8.1]

    test = filtrage.filtre_moyenne(donnees)
    test2 = filtrage.filtre_moyenne(donnees2)

    assert test == reponse, f"Erreur: {test} != {reponse}"
    assert test2 == reponse2, f"Erreur: {test2} != {reponse2}"
    
    pass

def test_filtre_mediane():

    donnees = [1,-1]
    donnees2 = [3,3.5,6,9,7.2]
    reponse=[1,-1]
    reponse2=[3,3.5,6,7.2,7.2]

    test = filtrage.filtre_mediane(donnees)
    test2 = filtrage.filtre_mediane(donnees2)

    assert test == reponse, f"Erreur: {test} != {reponse}"
    assert test2 == reponse2, f"Erreur: {test2} != {reponse2}"
    
    pass

    












#===========================================
if __name__ == "__main__":
    """
    DESC: Point d'entrée du programme
    """ 
    test_filtre_min_max()
    test_filtre_moyenne()
    test_filtre_mediane()

    
    print("Tous les tests ont réussi.")