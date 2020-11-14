from tkinter import *


# ====================================================
# fonction de hashage qui retourne l'adresse de la page où on va insérer les clés
def fonction_hashage(p, k, M):
    y = k % ((2 ** p) * M)
    return y


# ====================================================
# verifie si une page est pleine ou pas ( overflow)
def verification_vide(page, C):
    pas = 0
    for i in range(0, C):
        if page[i] == "Vide":
            pas = 1
    if pas == 1:
        return True
    else:
        return False


# ==================================================
def Redistribution_Function(list, indice, p, k, M, C):
    for i in range(0, C):
        redistribution = list[indice]  # la page contenant l'overflow
        if redistribution[i] != "Vide":  # on cherche les élements de la page overflow (non vide)
            k = redistribution[i]  # k parcours les elements de la page overflow
            pas = fonction_hashage(p, k, M)  # on cherche l' adresse
            ajout = list[int(pas)]  # la page qui correspond a l'adresse (pas)
            while True:
                if ajout[i] == "Vide":  # si la page contient un emplacement vide
                    ajout[i] = k  # on insere notre entier
                    break
                else:
                    ajout[
                        i] == k  # dans le cas contraire l'element reste à sa place (l'adresse reste la mm apres le hashage)
                    ajout[i] = k
                    break
            list[int(pas)] = ajout  # on place les valeurs
            if indice != pas:  # si l'element a été placé on le remplace par "vide"
                redistribution[i] = "Vide"
    list[indice] = redistribution
    return list


# ==================================================
#                     Main                        #
# ==================================================

M = int(input("Donner le nombre de pages :"))
C = int(input("Donner la capacité :"))

# Création du tableau initial
list = []
element = []
vectors = []

# Remplissage des listes
for i in range(0, M):
    for j in range(0, C):
        element.append("Vide")
    list.append(element)
    vectors.append(0)
    element = []

p = 0
# Moteur assignation des entiers
while True:
    print(list)
    print(vectors)
    ent = input("Donner l'entier a stocker (STOP pour arret):")
    if (ent == "STOP"):
        break
    else:
        ent = int(ent)
    while True:
        verif = 0
        for i in range(0, M):
            for j in range(0, C):
                if list[i][j] == ent:
                    verif = 1
        if verif == 1:
            ent = int(input("Vous avez déja saissi cette entier ! Recommencer :"))
        else:
            k = ent
            break
    indice = fonction_hashage(p, k, M)
    not_overflow = verification_vide(list[int(indice)], C)
    # Cas : Pas de overflow
    if not_overflow == True:
        ajout = list[int(indice)]#verification de la page dans laquelle on va inserer les elements
        pas = 0
        while True:
            if ajout[pas] == "Vide":
                ajout[pas] = k
                break
            else:
                pas += 1
        list[int(indice)] = ajout
    else:
        # Cas : Si il y'a un overflow
        print("Il y'a un Overflow : Restructuration de la table")
        p += 1 #on passe de H0 à H1
        #On double notre tableau
        for i in range(M, len(list) * 2):
            for j in range(0, C):
                element.append("Vide")
            list.append(element)
            vectors.append(0)
            element = []

        list = Redistribution_Function(list, indice, p, k, M, C)
        indice = fonction_hashage(p, k, M)
        not_overflow = verification_vide(list[int(indice)], C) #On verifie si la page contient un emplacement vide
        if not_overflow == True:
            ajout = list[int(indice)]
            pas = 0
            while True:
                if ajout[pas] == "Vide":
                    ajout[pas] = k
                    break
                else:
                    pas += 1
            list[int(indice)] = ajout
        else:
            # Exeption si erreur dans le programme car mathématiquement le nouveau emplacement ne doit etre sur un overflow
            print("Il y'a eu une erreur ! Arret du programme !")
            break
    # Verification liste vecteur : #1 si la liste est non vide ,0 sinon
    while True:
        verif = 0
        for i in range(0, len(list)):
            for j in range(0, C):
                if list[i][j] != 'Vide':
                    verif = 1
            if verif == 1:
                vectors[i] = 1
                verif = 0
        break
