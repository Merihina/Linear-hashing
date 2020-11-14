
def fonction_hashage(p,k,M):
    y=k%((2**p)*M)
    return y
#======================================================================================================================
def verification_vide(list,C):
    pas = 0
    for i in range(0,C):
        if list[i] == "Vide":
           pas = 1
    if pas == 1:
        return True
    else:
        return False
#=======================================================================================================================
#==================================================
def Redistribution_Function(list,indice,p,k,M,C):
    for i in range(0,C):
        redistribution = list[indice]
        if redistribution[i] != "Vide" :
            k = redistribution[i]
            nouveau_indice = fonction_hashage(p, k, M)
            ajout = list[int(nouveau_indice)]
            while True:
                if ajout[i] == "Vide":
                    ajout[i] = k
                    break
                else:
                    ajout[i] == k
                    ajout[i] = k
                    break
            list[int(nouveau_indice)] = ajout
            if indice !=nouveau_indice :
                redistribution[i] = "Vide"
    list[indice] = redistribution
    return list

#=======================================================================================================================
#==========================================================Main=========================================================
M = int(input("Donner le nombre de pages :"))
C = int(input("Donner la capacité :"))

#Création du tableau initial
list = []
list_overflow =[]
element = []

for i in range(0,M):
    for j in range(0,C):
        element.append("Vide")
    list.append(element)
    element = []

for i in range(0,M):
    for j in range(0,C):
        element.append("Vide")
    list_overflow.append(element)
    element = []

p = 0
pointeur=0
while True:
    if pointeur > M :
        p += 1
        pointeur = 0
    print(list)
    for i in range(0, len(list_overflow)):
        for j in range(0, C):
            if list_overflow[i][j] != 'Vide':
                print("Overflow stocké Case N°",i," contenant :",list_overflow[i][j])

    print("Position Pointeur Case N°", pointeur)
    ent=input("Donner l'entier a stocker (STOP pour arret):")
    if(ent=="STOP"):
        break
    else :
        ent = int(ent)
    while True :
        verif = 0
        for i in range(0, M):
            for j in range(0, C):
                if list[i][j] == ent :
                    verif = 1
        if verif == 1 :
            ent = int(input("Vous avez déja saissi cette entier ! Recommencer :"))
        else :
            k = ent
            break
    indice = fonction_hashage(p,k,M)
    not_overflow = verification_vide(list[int(indice)],C)
    if not_overflow == True :
        ajoute = list[int(indice)]
        pas = 0
        while True :
            if ajoute[pas] == "Vide" :
                ajoute[pas] = k
                break
            else :
                pas += 1
        list[int(indice)] = ajoute
    else : #    Il y a un overflow
        print("Il y'a un Overflow : Restructuration de la table")
        p=p+1
        for i in range(M,M+1):
            for j in range(0, C):
                element.append("Vide")
            list.append(element)
            element = []
        for i in range(M,M+1):
            for j in range(0, C):
                element.append("Vide")
            list_overflow.append(element)
            element = []
        list = Redistribution_Function(list,pointeur, p, k, M, C)
        ajout = list_overflow[int(indice)]
        pas = 0
        while True:
                    if ajout[pas] == "Vide":
                        ajout[pas] = k
                        break
                    else:
                        pas += 1
        list_overflow[int(indice)] = ajout
        p = p-1
        pointeur += 1

