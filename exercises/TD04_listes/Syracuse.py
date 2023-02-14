def syracuse(n: int)->list:
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste=[n]
    while n!= 1:
        if n%2==0:
          n=n//2
        else:
            n=n*3+1
        liste.append(n)
    return liste

print(syracuse(3))

def testeConjecture(n_max: int)->bool:
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range(1,n_max+1):
        # On appelle simplement la fonction, sans
        # Si le programme sort de l'appel à la fonction 
        # dernier nombre était 1. Sinon syracuse d
        syracuse(i)
    return True
print(testeConjecture(10000))
def tempsVol(n):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return len(syracuse(n))-1

print("le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max: int)-> list:
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return[tempsVol(i)for i in range(1,n_max+1)]

print(tempsVolListe(100))

#On liste les temps de vols de tous les entiers entre 1 
liste_temps=tempsVolListe(10000)

#Avec la fonction max(), on trouve le temps de vol maximal
temps_max=max(liste_temps)

#on affiche l'entier correspondant à ce temps de vol
print("L'entier", liste_temps.index(temps_max)+1, "a le plus grand temps de vol égal à",temps_max)

def altMax(n:int)->int:
    """Retourne l'entier maximal """
    return max(syracuse(n))

def altMaxListe(n_max:int)->list:
    """Retourne la liste des altitudes maximales des entiers"""
    return[altMax(i)for i in range(1, n_max+1)]

list_alt=altMaxListe(10000)
altitude_max=max(list_alt)
print("L'entier", list_alt.index(altitude_max)+1, "a la plus grande altitude maximale égale à", altitude_max)