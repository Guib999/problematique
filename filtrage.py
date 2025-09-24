"""
GRO120: Module filtrage - implémentation des filtres à appliquer sur les données lidar 

Auteurs: Guillaume Larouche et Simon Côté
Date: 24/09/2025
""" 



def filtre_min_max(points, distance_min=0.5, distance_max=15):
    """
    DESC: Filtre les points en éliminant ceux qui sont hors des bornes min/max.
          Les valeurs inférieures à la borne min sont remplacées par -1.
          Les valeurs supérieures à la borne max sont remplacées par max.
          
    RETOUR: Tableau de données filtrées
    """
    
    
    for i in range(0, len(points)): 
        
        if points[i]<distance_min:
            points[i] = -1
        if points[i] > distance_max:
            points[i] =distance_max
    


    return points




def filtre_moyenne(points):
    """
    DESC: Filtre qui change les données pour la moyenne de la données en question et de celle directement avant et après
        dans un tableau de données 
          
    RETOUR: Tableau de données filtrées
    """

    points2= []
    for i in range(0, len(points)):
        
        
        if i == 0 :
            moyenne= (points[i]+points[i+1])/2              #Considère la différence de calcule entre les données 
            points2.append(round(moyenne, 1))               #des extrémité et ceux de l'intérieur
        elif i == len(points)-1 :
            moyenne= (points[i-1]+points[i])/2
            points2.append(round(moyenne, 1))
        else:
            moyenne= (points[i-1]+points[i]+points[i+1])/3
            
            points2.append(round(moyenne, 1))
 


    return points2

def filtre_mediane(points):
    """
    DESC: Filtre qui change les données du lidar pour la mediane de la donnée en question et de celle directement avant et après
        dans un tableau de données sauf les valeurs au extrémiter qui reste pareil.
          
    RETOUR: Tableau de données filtrées
    """
    points2=[]
    for i in range(0, len(points)):                     #Considère la différence d'action entre les données 
        if i==0 or i==len(points)-1:                    #des extrémité et ceux de l'intérieur
            points2.append(points[i])
        else:
            tmp =[points[i-1], points[i],points[i+1]]
            tmp.sort()  
            points2.append(tmp[1])



    return points2

def filtre_bonne_valeur(points):
    """
    DESC: Filtre qui retire tout les mauvaises données d'un tableau des données du lidar
          
    RETOUR: Tableau de données filtrées
    """
    bonV =[]
    for p in points:
        if p>-1:
            bonV.append(p)
    
    return bonV


