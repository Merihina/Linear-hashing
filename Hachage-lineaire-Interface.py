from tkinter import *
from tkinter import messagebox


#====================================================
def fonction_hashage(k):
    y=k%((2**p)*M)
    return y

#====================================================
def verification_vide(list):
    pas = 0
    for i in range(0,C):
        if list[i] == "Vide":
           pas = 1
    if pas == 1:
        return True
    else:
        return False
#==================================================
def Redistribution_Function(list,indice,k):
    for i in range(0,C):
        redistribution = list[indice]
        if redistribution[i] != "Vide" :
            k = redistribution[i]
            pas = fonction_hashage(k)
            ajout = list[int(pas)]
            while True:
                if ajout[i] == "Vide":
                    ajout[i] = k
                    break
                elif ajout[i] == k:
                    ajout[i] = k
                    break
                else:
                    pas += 1
            list[int(pas)] = ajout
            if indice != pas :
                redistribution[i] = "Vide"
    list[indice] = redistribution
    return list

#==================================================
#Createur de la liste page
def List_Generator(M,C):
    list = []
    element = []

    # Remplissage des listes
    for i in range(0, M):
        for j in range(0, C):
            element.append("Vide")
        list.append(element)
        element = []
    return list

#==================================================
#Createur de la liste Overflow
def list_overflow_Generator(M,C):
    list_overflow = []
    element = []

    # Remplissage des listes
    for i in range(0, M):
        for j in range(0, C):
            element.append("Vide")
        list_overflow.append(element)
        element = []
    return list_overflow


#================================================
#Vider la Page (Interface Graphique)
def delete_frame(x):
    for widget in fenetre.winfo_children():
        if x == 1 :
            widget.pack_forget()
        else :
            widget.destroy()

#================================================
#Moteur d'affichage (Interface Graphique)
def affichage(list,list_overflow):
    M = len(list)
    C = len(list[0])

    canvas = Canvas(fenetre, height=100, width=100, bg='Blue')
    canvas.grid(row=2, column=pointeur + 1)
    champ = Label(fenetre, text="Pointeur")
    champ.grid(row=2, column=pointeur + 1)

    champ_label2 = Label(fenetre, text="Etat des Pages")
    champ_label2.grid(row=3, column=0)
    for i in range(0, M):
        test = "|"
        canvas = Canvas(fenetre, height=100, width=100, bg='pink')
        canvas.grid(row=3, column=i+1)
        for j in range(0,C):
            test = test + str(list[i][j]) + "|"
        champ = Label(fenetre, text=test)
        champ.grid(row=3, column=i+1)
    for i in range(0, M):
        for j in range(0, C):
            if list_overflow[i][j] != 'Vide':
                canvas = Canvas(fenetre, height=100, width=100, bg='green')
                canvas.grid(row=4, column=i+1)
                champ = Label(fenetre, text=list_overflow[i])
                champ.grid(row=4, column=i+1)

#==================================================
#Verificateur de p
def verificateur():
    global pointeur
    if pointeur > M :
        global p
        p += 1
        pointeur = 0

# ================================================
# Processus de stockage (Interface Graphique)
def Hash(k,list,list_overflow):
    indice = fonction_hashage(k)
    overflow = verification_vide(list[indice])
    global p
    global pointeur
    p = 0
    verificateur()
    if overflow == True:
        ajout = list[int(indice)]
        pas = 0
        while True:
            if ajout[pas] == "Vide":
                ajout[pas] = k
                break
            else:
                pas += 1
        list[int(indice)] = ajout
    else :
        # Cas : Si il y'a un overflow
        champ_label2 = Label(fenetre, text="Overflow", font=("Arial Bold", 10))
        champ_label2.grid(row=5, column=2)
        ajout = list_overflow[int(indice)]
        pas = 0
        while True:
            if ajout[pas] == "Vide":
                ajout[pas] = k
                break
            else:
                pas += 1
        list_overflow[int(indice)] = ajout
        p = p + 1
        pointeur = pointeur + 1
        element = []
        for i in range(M, M+1):
            for j in range(0, C):
                element.append("Vide")
            list.append(element)
            element = []
        for i in range(M, M+1):
            for j in range(0, C):
                element.append("Vide")
            list_overflow.append(element)
            element = []

        list = Redistribution_Function(list, indice,k)
        indice = fonction_hashage(k)
        p = p - 1

    global g_list2
    g_list2 = list
    global g_overflow2
    g_overflow2 = list_overflow
    affichage(list, list_overflow)
    champ_label2 = Label(fenetre, text="Entier à stocker", font=("Arial Bold", 10))
    champ_label2.grid(row=5, column=0)
    global entier
    g_k = StringVar()
    entier = Entry(fenetre, textvariable=g_k, width=30)
    entier.grid(row=6, column=0)
    btn = Button(fenetre, text="Stocké", command=Vérificateur_doublon)
    btn.grid(row=7, column=0)

#================================================
#Alerte si doublon de saisi Entier (Interface Graphique)
def Vérificateur_doublon():
    k = int(entier.get())
    list = g_list
    while True:
        verif = 0
        for i in range(0, M):
            for j in range(0, C):
                if list[i][j] == k:
                    verif = 1
        if verif == 1:
            messagebox.showwarning("Doublon", "Vous avez déja saissi cette Entier")
        else :
            delete_frame(0)
            Hash(k,g_list2,g_overflow2)
        break

#================================================
#Prmiére assignation avant Boucle (Interface Graphique)
def First():
    k = int(entier.get())
    delete_frame(0)
    Hash(k,g_list,g_overflow)

#================================================
#Bouton Execution (Interface Graphique)
def clicked():

    global pointeur
    pointeur = 0
    global M
    M = int(page.get())
    global C
    C = int(capacite.get())
    global p
    p = 0
    delete_frame(1)
    list = List_Generator(M,C)
    global g_list
    g_list = list
    list_overflow = list_overflow_Generator(M,C)
    global g_overflow
    g_overflow = list_overflow
    affichage(list,list_overflow)
    champ_label2 = Label(fenetre, text="Entier à stocker", font=("Arial Bold", 10))
    champ_label2.grid(row=5, column=0)
    global entier
    g_k = StringVar()
    entier = Entry(fenetre, textvariable=g_k, width=30)
    entier.grid(row=6, column=0)
    btn = Button(fenetre, text="Stocké", command=First)
    btn.grid(row=7, column=0)


#================================================
#Interface Graphique
fenetre = Tk()
fenetre.title("Hashage Linéaire")
fenetre.geometry('1200x600')
champ_label = Label(fenetre, text="Hashage Linéaire", font=("Arial Bold", 25))
champ_label.pack()
champ_label1 = Label(fenetre, text="")
champ_label1.pack()
champ_label2 = Label(fenetre, text="Nombre de page initiale")
champ_label2.pack()
var_page = StringVar()
page = Entry(fenetre, textvariable=var_page, width=30)
page.pack()
champ_label3 = Label(fenetre, text="Capacité de la case")
champ_label3.pack()
var_capacite = StringVar()
capacite = Entry(fenetre, textvariable=var_capacite, width=30)
capacite.pack()
btn = Button(fenetre, text="Execution", command=clicked)
btn.pack()
fenetre.mainloop()


