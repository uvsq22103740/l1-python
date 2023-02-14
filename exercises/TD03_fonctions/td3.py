from ast import Return

import time

def tempsEnSeconde(temps: tuple) -> int:
    """ Renvoie la valeur en seconde de temps donné comme jour,
     heure, minute, seconde. """
    return temps[0]*3600*24+temps[1]*3600+temps[2]*60+temps[3]


temps = (3, 23, 1, 34)
print(type(temps))
print(tempsEnSeconde(temps))

def affichePluriel(mot:str,nombre:int)->None:
    """Affiche (ou non) un mot en fonction du paramètre nombre.
    Met le mot au pluriel si nécessaire"""
    if nombre>0:
        print(" ",nombre, mot,end="")

    if nombre>1:
        print("s",end="")

def afficheTemps(temps):
    affichePluriel("jour", temps[0])
    affichePluriel("heure", temps[1])
    affichePluriel("minute", temps[2])
    affichePluriel("seconde", temps[3])
    print()
##afficheTemps((1,0,14,23))

def demandeTemps()->tuple:
    """Demande à l'utilisateur un nombre de jours, d'heures, de
    minutes et desecondes et les renvoie sous la forme d'un tuple de temps"""
    jours = -1
    heures = -1
    minutes = -1
    secondes = -1
    while (jours < 0):
        jours = int(input("entrez un nombre de jours"))
    while (heures<0) or (heures >= 24):
        heures = int(input("Entrez un nombre d'heures"))
    while (minutes <0) or (heures >= 60):
        minutes = int(input("Entrez un nombre de minutes"))
    while (secondes<0) or (secondes >= 60):
        secondes = int(input("Entrez un nombre de secondes"))

    temps=(jours,heures,minutes,secondes)
    return temps

temps=demandeTemps()
print(temps)
print(tempsEnSeconde(temps))

def secondesEnTemps(t):
    jours=int(t/(3600*24))
    heure = int((t-jours*3600*24)/3600)
    minute = int((t-3600*heure-jours*3600*24)/60)
    secondes = int(t-(3600*heure)-(60*minute)-jours*3600*24)
    temps = (jours,heure, minute, secondes)
    return temps

def sommeTemps(temps1: tuple, temps2:tuple) -> tuple:
    return secondesEnTemps(tempsEnSeconde(temps1)+tempsEnSeconde(temps2))

afficheTemps(sommeTemps((2, 3, 4, 25), (5, 22, 57, 1)))

def proportionTemps(temps : tuple, proportion : float) -> tuple:
    return secondesEnTemps(tempsEnSeconde(temps)*proportion)

def tempsEnDate(temps : tuple) -> tuple:
    """Retourne un tuple contenant la date obtenue en ajoutant
    la durée stockée dans le paramètre temps au 1er janvier 1970.
    Ne prend pas en compte les années bisextiles"""
    annee = 1970 + temps[0]//365
    numero_du_jour = 1 + temps[0]%365
    return(annee, numero_du_jour, temps[1], temps[2], temps[3])

def afficheDate(date: tuple=())->None:

    if len(date)==0:
        date=tempsEnDate(secondesEnTemps(int(time.time())))
    print("jour nuléro", date[1], "de l'année", date[0], "à", str(date[2])+":"+ str(date[3]) +":"+ str(date[4]))