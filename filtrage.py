"""
GRO120: Module filtrage - implémentation des filtres à appliquer sur les données lidar 

Auteurs: ...
Date: jj/mm/aaaa
""" 


#===========================================
def filtre_min_max(points, distance_min=0.5, distance_max=15):
    """
    DESC: Filtre les points en éliminant ceux qui sont hors des bornes min/max.
          Les valeurs inférieures à la borne min sont remplacées par -1.
          Les valeurs supérieures à la borne max sont remplacées par max.
          
    RETOUR: Tableau de données filtrées
    """
    
    # Code à compléter
    for i in range(0, len(points)):
        
        if points[i]<distance_min:
            points[i] = -1
        if points[i] > distance_max:
            points[i] =distance_max
    


    return points


#===========================================
# Autres fonctions à compléter...
#===========================================

def filtre_moyenne(points):
    points2= []
    for i in range(0, len(points)):
        
        
        if i == 0 :
            moyenne= (points[i]+points[i+1])/2
            points2.append(round(moyenne, 1))
        elif i == len(points)-1 :
            moyenne= (points[i]+points[i-1])/2
            points2.append(round(moyenne, 1))
        else:
            moyenne= (points[i]+points[i-1]+points[i+1])/3
            
            points2.append(round(moyenne, 1))



    return points2

def filtre_mediane(points):

    points2=[]
    for i in range(0, len(points)):
        if i==0 or i==len(points)-1:
            points2.append(points[i])
        else:
            tmp =[points[i-1], points[i],points[i+1]]
            for i in range(0, len(tmp)-1): 
                indexMIN=i
                for j in range(i+1, len(tmp)):
                    if tmp[indexMIN]> tmp[j]:
                        indexMIN= j

                tmp[i], tmp[indexMIN]= tmp[indexMIN],tmp[i]     
            points2.append(tmp[1])



    return points2

def filtre_bonne_valeur(points):
    bonV =[]
    for p in points:
        if p!=-1:
            bonV.append(p)
    
    return bonV


