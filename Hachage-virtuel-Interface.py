from tkinter import *
from tkinter import messagebox

#===================================================
def verification_vide(list):
    for i in range(0,len(list)):
        pas = 0
        if list[i] == "Vide":
           pas = 1
    if pas == 1:
        return True
    else:
        return False

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
#Verification liste vecteur
def Vectors(list,vectors):
    while True :
        verif = 0
        for i in range(0, len(list)):
            for j in range(0, C):
                if list[i][j] != 'Vide' :
                    verif = 1
                if verif == 1 :
                    vectors[i] = 1
                    verif = 0
        break
    return vectors

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
#Createur de la liste vecteurs
def Vectors_Generator(M):
    Vector = []
    # Remplissage des listes
    for i in range(0, M):
        Vector.append("0")
    return Vector


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
def affichage(list,vectors):
    M = len(list)
    C = len(list[0])
    champ_label2 = Label(fenetre, text="Etat des Pages")
    champ_label2.grid(row=2, column=0)
    for i in range(0, M):
        test = "|"
        canvas = Canvas(fenetre, height=100, width=100, bg='pink')
        canvas.grid(row=2, column=i+1)
        for j in range(0,C):
            test = test + str(list[i][j]) + "|"
        champ = Label(fenetre, text=test)
        champ.grid(row=2, column=i+1)
    champ_label2 = Label(fenetre, text="Etat vecteurs")
    champ_label2.grid(row=3, column=0)
    for i in range(0, M):
        canvas = Canvas(fenetre, height=100, width=100, bg='green')
        canvas.grid(row=3, column=i+1)
        champ = Label(fenetre, text=vectors[i])
        champ.grid(row=3, column=i+1)


# ================================================
# Processus de stockage (Interface Graphique)
def Hash(k,list,vectors):
    indice = fonction_hashage(k)
    overflow = verification_vide(list[indice])
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
        global p
        p += 1
        element = []
        for i in range(M, len(list) * 2):
            for j in range(0, C):
                element.append("Vide")
            list.append(element)
            vectors.append(0)
            element = []

        list = Redistribution_Function(list, indice,k)
        indice = fonction_hashage(k)
        overflow = verification_vide(list[int(indice)])
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
    vectors = Vectors(list, vectors)
    global g_list2
    g_list2 = list
    global g_vector2
    g_vector2 = vectors
    affichage(list, vectors)
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
            Hash(k,g_list2,g_vector2)
        break

#================================================
#Prmiére assignation avant Boucle (Interface Graphique)
def First():
    k = int(entier.get())
    delete_frame(0)
    Hash(k,g_list,g_vector)

#================================================
#Bouton Execution (Interface Graphique)
def clicked():
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
    vectors = Vectors_Generator(M)
    global g_vector
    g_vector = vectors
    affichage(list,vectors)
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
fenetre.title("Hashage Virtuel")
fenetre.geometry('1200x600')
champ_label = Label(fenetre, text="Hashage Virtuel", font=("Arial Bold", 25))
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


