# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 23:08:00 2018

@author: Inestelle
"""

############################################################################################################################
#%% importation de module pour realiser le projet ##########################################################################
############################################################################################################################ 
import csv
import numpy as np
import sys
import matplotlib.pyplot as plt

############################################################################################################################
#%% Affichage début code ###################################################################################################
############################################################################################################################ 

def stop(): #fonction permettant de stopper ou non 
    a = str(input("Souhaitez-vous continuer : o ou n ? Ou revoir toutes les fonctions disponibles : p ?"))
    if a == "o" : #si l'utilisateur tape "o", les fonctions continuent
        pass
    elif a == "p" :
        print("Voici les fonctions existantes :")
        print("maj_tout(T,o) : T la liste des données et o la liste des plafonds. Permet de convertir toutes les notes supérieures au plafond, au plafond.")
        print("major(T,n) : T la liste des données.")
        print("print_oui_ou_non(name,T) : name le prenom de l'etudiant, T la liste des données. Permet de savoir quel élève a eu son UE.")
        print("moy_colonne(n) : n la colonne. Permet d'avoir la moyenne d'un thème.")
        print("moy_eleve(name,T,c) : name le prenom de l'etudiant, T la liste des données, c le coefficient total. Permet d'obtenir la moyenne (en xp) de son UE.")
        print("note(xp,AAsur450) : xp le nombre d'xp, AAsur450 la liste des paliers des xp correspondant à une note sur 20. Permet d'obtenir la conversion de points xp en note sur 20.")
        print("courbe_nbXP_note20(plafond) : plafond le max d'xp. Obtention d'une courbe nXP/notre20.")
        print("note_sur_20_eleve(T,P,name) : name le prenom de l'etudiant, T la liste des données, c le coefficient total. Permet d'obtenir la note sur 20 d'un élève.")
        print("notes_sur_20() :  ")
        print("graph_notes_sur_20() :  ")
        print("fiche_eleve(name,T,c): name le prenom de l'etudiant, T la liste des données, c le coefficient total. Obtention d'une fiche complête d'un etudiant.")
        print("camembertNotes()")
        print("theme(): permet d'afficher des histogrammes !")
        pass
    else : #sinon ça ferme la fenêtre
        sys.exit(0) 



print("Bonjour! Bienvenue sur notre plateforme interactive !")
a = str(input("Pour bien commencer, veuillez cliquer sur 'p' si vous ne connaissez pas les fonctions existantes, sinon tapez 'c' :"))
if a == "c" : #si l'utilisateur tape "c", les fonctions continuent
    pass
elif a == "p" : #et si l'utilisateur tape "p"
    print("Voici les fonctions existantes :")
    print("maj_tout(T,o) : T la liste des données et o la liste des plafonds. Permet de convertir toutes les notes supérieures au plafond, au plafond.")
    print("major(T,n) : T la liste des données.")
    print("print_oui_ou_non(name,T) : name le prenom de l'etudiant, T la liste des données. Permet de savoir quel élève a eu son UE.")
    print("moy_colonne(n) : n la colonne. Permet d'avoir la moyenne d'un thème.")
    print("moy_eleve(name,T,c) : name le prenom de l'etudiant, T la liste des données, c le coefficient total. Permet d'obtenir la moyenne (en xp) de son UE.")
    print("note(xp,AAsur450) : xp le nombre d'xp, AAsur450 la liste des paliers des xp correspondant à une note sur 20. Permet d'obtenir la conversion de points xp en note sur 20.")
    print("courbe_nbXP_note20(plafond) : plafond le max d'xp. Obtention d'une courbe nXP/notre20.")
    print("note_sur_20_eleve(T,P,name) : name le prenom de l'etudiant, T la liste des données, c le coefficient total. Permet d'obtenir la note sur 20 d'un élève.")
    print("notes_sur_20() :  ")
    print("graph_notes_sur_20() :  ")
    print("fiche_eleve(name,T,c): name le prenom de l'etudiant, T la liste des données, c le coefficient total. Obtention d'une fiche complête d'un etudiant.")
    print("camembertNotes()")
    print("theme(): permet d'afficher des histogrammes !")
    pass
stop()

############################################################################################################################
#%% Récupération du fichier ################################################################################################
############################################################################################################################

with open('donnees_projet', 'r') as f: #ourvir le fichier qui se trouve au meme emplacement que ce fichier .py
    reader = csv.reader(f) #retourne un objet "lecteur" qui va iterer sur les lignes dans le fichier csv donne. 
    your_list = list(reader) #transforme en liste

entete = your_list.pop(0) #supprime la premiere ligne d'entete du tableau
T = np.array(your_list).astype(np.float) #transforme tous les elements du tableau (string) en float


############################################################################################################################
#%% Programme permettant de mettre les notes superieures au plafond ########################################################
############################################################################################################################
"""
for i in range (len(T)): #pour tous les i appartenant a  l'intervalle [nombre d'elements du tableau T]
#si l'element est superieur a  50, alors cet element prend comme valeur 50   
    if T[i,0] > 50 : 
        T[i,0]=50   

for i in range (len(T)):
    if T[i,1] > 100 :
        T[i,1]=100
        
for i in range (len(T)):
    if T[i,2] > 100 :
        T[i,2]=100

for i in range (len(T)):
    if T[i,3] > 200 :
        T[i,3]=200
        
#print(T)   
"""

o = [50,100,100,200] #liste des differents plafonds de notes


def maj(T,o,n): #fonction mettant toutes les notes superieures au plafond au plafond (pour une colonne)
    #T la liste, o liste des plafonds, n le numéro de la colonne
    for i in range (len(T)): #pour tous les i appartenant a l'intervalle [nombre d'emplacement du tableau T]
    #si l'emplacmeent est superieur a 50, alors cet element prend comme valeur le plafond   
        if T[i,n] > o[n] : 
            T[i,n]= o[n] 
    return T
    stop()
    

    
def maj_tout(T,o): #fonction mettant toutes les notes superieures au plafond au plafond pour tout le tableau
    #T la liste, o liste des plafonds, n le numéro de la colonne
    n=0
    while n<len(o):
        T=maj(T,o,n)
        n+=1
    return T
    stop()

############################################################################################################################
#%% Fonction permettant de terminer le major de chaque theme ###############################################################
############################################################################################################################

#Nos remerciements vont au groupe de Quentin, Matthieu et Mickaël, pour leur aide à la réalisation de cette fonction
def major (T,n): #fonction determinant le major de la classe
    tt = []
    for i in T :
        tt.append([i[n]]) #ajoute un element en fin de liste
    for j in range (len(tt)):
        tt[j].append(j) #ajoute un element en fin de liste
    tt = sorted(tt) #renvoie une nouvelle liste tt triee
    tt = tt[::-1] #inverse la liste (croissante --> decroissante) 
    print(tt[1])
    stop()


############################################################################################################################
#%% Attribution de chaque ligne de notes a un eleve ######################################################################## 
############################################################################################################################

P = ["Jean","Pierre","Michel","Andre","Philippe","Rene","Louis","Alain",\
     "Jacques","Bernard","Marcel","Daniel","Roger","Robert","Claude","Paul",\
     "Christian","Henri","Georges","Nicolas","Francois","Patrick","Gerard",\
     "Christophe","Joseph","Julien","Maurice","Laurent","Frederic","David",\
     "Stephane","Pascal","Sebastien","Alexandre","Thierry","Olivier","Thomas",\
     "Raymond","Antoine","Guy","Dominique","Charles","Didier","Marc","Vincent",\
     "Yves","Guillaume","Bruno","Serge","Maxime","Marie","Jeanne","Claude",\
     "Francoise","Monique","Catherine","Nathalie","Isabelle","Jacqueline",\
     "Anne","Sylvie","Martine","Madeleine","Nicole","Suzanne","Helene",\
     "Christine","Marguerite","Denise","Christiane","Yvonne","Louise",\
     "Valerie","Sophie","Dominique","Sandrine","Stephanie","Celine",\
     "Veronique","Chantal","Marcelle","Renee","Simone","Jeannine","Paulette",\
     "Julie","Annie","Patricia","Brigitte","Lucie","Camille","Lea","Alice",\
     "Aurelie","Laurence","Michele","Cecile","Therese","Colette","Virginie"]

"""
name = input("Entrez le nom de l'eleve dont vous voulez connaitre les notes : \n") 
                                    #Association d'un eleve a ses notes d'UE. Merci Philippe :)
rang = -1
if name in P:
    rang = P.index(name)
    print(name,"a obtenu les notes",T[rang]) 
            #Enlever la derniere colonne et ajouter des lignes pour savoir si l'eleve a valide son UE
else:
    print("Vous ne connaissez pas vos eleves ? :( Entrez le nom d'un de vos eleves")
 """   
    
 
def nametorang(name):
    if name in P:
        return P.index(name) #retourne le rang du prenom de l'etudiant
    else:
        return "Erreur"
        

############################################################################################################################
#%% Quels élèves ont eu leur semestre ? #################################################################################### 
############################################################################################################################     
    
def oui_ou_non(name,T): #savoir si l'etudiant a son UE ou non
    if nametorang(name) != "Erreur": #verification si prenom present dans la liste
        rang = nametorang(name)
        if T[rang,4] == 1.0: #si l'etudiant a son UE, 1.0
            return True
        else :
            return False
    else:
        return None
    stop()
 

       
def print_oui_ou_non(name,T): #affichage de la fonction precedente
    if oui_ou_non(name,T) == True :
        print(name, "a eu son semestre !")
    elif oui_ou_non(name,T) == False :
        print(name,"n'a pas eu son semestre, et doit passer les rattrapages ...")
    else :
        print("Erreur")
    stop()



def oui_ou_non_tous(P,T): #affichage de tous les étudiants ayant leur UE et ceux ne l'ayant pas eu !
    r = []
    g = []
    for i in range (len(T)):
        if oui_ou_non(P[i],T):
            r.append(P[i]) 
    return r
    stop()


############################################################################################################################
#%% Moyenne pour un theme colonne n ########################################################################################
############################################################################################################################

def moy_colonne(n):
    moy = np.mean(T,0)[n]
    print("La moyenne de cette UE est de",moy)
    stop()
    
############################################################################################################################   
#%% Moyenne de chaque eleve ################################################################################################
############################################################################################################################ 
def moy_eleve(name,T,c):  #e : numéro de ligne du tableau et c : Coefficient ici 9
    m=0
    if nametorang(name) != "Erreur":
        rang = nametorang(name)
        for i in range(len(T[rang])):
            m += T[rang][i]  #rang i dans la liste e (ligne du tableau) de la liste T
        m = m/c #On considère qu'une note sur 50 a un coefficient 1 dans notre cas actuel
        return m
    else:
        print("Erreur")
    stop()


############################################################################################################################   
#%% Conversion nb XP <=> note sur 20 #######################################################################################
############################################################################################################################ 

AA = [0,3,8,16,25,36,48,62,78,94,112,131,151,172,194,218,243,267,294,321,350]
BB = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

AAsur450 = [9/7*e for e in AA] #liste AA convertissant les XP sur 450 (x un facteur !)


def indexmin(AAsur450,xp):
    i = 0
    while xp > AAsur450[i] :
        i += 1
        # if i > len(AAsur450) : error
    return i - 1
#print(indexmin(AAsur450,23))


def arrondir(xp,n): # arrondi a n chifres apres la virgule...
    return int(xp*10**n)/10**n


def entier(notes): #prendre la partie entière de toutes les notes qui sont float de base
    notes2 = []
    for i in range(len(notes)):
        x=notes[i]
        notes2.append(int(x))
    return notes2


def note(xp,AAsur450): #convertit le nombre d'XP en une note sur 20 arrondi à 2 chiffres après la virgule
    m1 = indexmin(AAsur450,xp)
    m2 = m1 + 1
    xp1 = AAsur450[m1]
    xp2 = AAsur450[m2]
    dm = 1
    dxp = xp2 - xp1
    a = dm/dxp
    b = m1 - xp1*a
    m = a*xp + b
    return arrondir(m,2)
    stop()

def courbe_nbXP_note20(plafond): #affiche la courbe pallier/note sur 20
    x = np.linspace(0,plafond+30,10)
    plt.plot(AA,BB,"+")
    plt.ylabel('Nombre de XP')
    plt.xlabel('Note sur 20')
    plt.show()
    stop()
    
    
tabsommexp = [sum(c[:-1]) for c in maj_tout(T,o)] #fait la somme de tous les éléments du tableau avec les notes qui ne peuvent pas être supérieures au plafond
notes = [note(xp,AAsur450) for xp in tabsommexp] #convertit le somme de ces xp en note sur 20


def note_sur_20_eleve(T,P,name):
    if nametorang(name) != "Erreur": #verification si prenom present dans la liste
        rang = nametorang(name)
        tabsommexp = [sum(T[rang,:-1])] #fait la somme de la ligne du rang correspondant
        notes = [note(xp,AAsur450) for xp in tabsommexp] #convertit le somme de ces xp en note sur 20
        return notes
    else :
        return "Erreur"
    stop()
    
    
def notes_sur_20(): #affiche un graphique avec un nuage de points (élèves ayant au dessus de la moyenne et en dessous)
    tabsommexp = [sum(c[:-1]) for c in maj_tout(T,o)] #fait la somme de tous les éléments du tableau avec les notes qui ne peuvent pas être supérieures au plafond
    notes = [note(xp,AAsur450) for xp in tabsommexp] #convertit le somme de ces xp en note sur 20
    notes2 = entier(notes) #ne prend que la partie entière de ces notes
    compteur_sup = 0
    compteur_inf = 0
    for nt in notes2 : #compteur eleves sup/egal et inf à 10
        if nt >= 10 :
            compteur_sup += 1
        else :
            compteur_inf += 1
    return compteur_sup,compteur_inf
    stop()
    
 
def graph_notes_sur_20():
    notes_sur_20()
    notes.sort()
    plt.plot([0,100],[10,10],'-')
    plt.plot(range(len(notes)),notes,'+')
    plt.show() 
    stop()
    
    
"""#convertit les notes XP en note 20
def convertion_notes_item(T,n) :
    AA = [0,3,8,16,25,36,48,62,78,94,112,131,151,172,194,218,243,267,294,321,350]
    AAsur450 = [(n/350)*e for e in AA]
    t = []
    for i in range(len(T[0])):
        np = note(T[i,0],AAsur450)
        t.append(nf)
    return t
"""
  
############################################################################################################################   
#%% Affiche fiche élève avec prénom, rang, nbXP par thème, moyenne, note finale sur 20 #####################################
############################################################################################################################    

def fiche_eleve(name,T,c): #création d'une fiche élève avec son prenom, son rang, ses notes, sa moyenne de l'UE
    if nametorang(name) != "Erreur": #verification si prenom present dans la liste
        rang = nametorang(name)
        moyenne = moy_eleve(name,T,c)
        note = note_sur_20_eleve(T,P,name)
        print(name, rang, " : Les notes de cette eleve sont ",T[rang],", sa moyenne est de ",moyenne, "avec une note de ",note,"sur 20")
    else:
        print("Erreur")
    stop()
    
    
############################################################################################################################   
#%% Affiche un camembert des élèves au-dessus de la moyenne et en dessous  #################################################
############################################################################################################################

def camembertNotes():
    labels = 'Supérieur à 10', 'Inférieur à 10'
    sizes = list(notes_sur_20()) #liste des bornes sup et inf (cf fonction notes_sur_20)
    explode = (0, 0.3)  # Met en exergue les 10% en dessous de la moyenne
    
    fig, camembert = plt.subplots()
    camembert.pie(sizes, labels=labels, explode=explode, shadow=True)
    camembert.axis('equal') #Permet d'avoir un beau camembert circulaire. =D

    plt.show()
    stop()
    
############################################################################################################################   
#%% Histogramme répartition élèves selon nombre d'XP dans chaque thème  ####################################################
############################################################################################################################ 

"""def theme1():    
    L1 = [row[0] for row in T] #Récupère la première colonne de T dans la liste L1 
                                #correspondant aux notes du 1er thème
    xmin = 0
    xmax = 50
    ymin=0
    ymax=25
    
    fig, hist_xp = plt.subplots()
    
    plt.hist(L1)
    hist_xp.set_xlim(xmin,xmax)
    hist_xp.set_ylim(ymin,ymax)
    hist_xp.set_xlabel("Nombre d'XP Thème 1")
    hist_xp.set_ylabel("Nombre d'élèves")
    hist_xp.set_title("Répartition des élèves selon leur nombre d'XP au thème 1")
    
    plt.show()
    stop()

def theme2():    
    L2 = [row[1] for row in T]
    xmin = 0
    xmax = 100
    ymin=0
    ymax=20
    
    fig, hist_xp = plt.subplots()
    
    plt.hist(L2)
    hist_xp.set_xlim(xmin,xmax)
    hist_xp.set_ylim(ymin,ymax)
    hist_xp.set_xlabel("Nombre d'XP Thème 2")
    hist_xp.set_ylabel("Nombre d'élèves")
    hist_xp.set_title("Répartition des élèves selon leur nombre d'XP au thème 2")
    
    plt.show()
    stop()
    
def theme3():    
    L3 = [row[2] for row in T]
    xmin = 0
    xmax = 100
    ymin=0
    ymax=25
    
    fig, hist_xp = plt.subplots()
    
    plt.hist(L3)
    hist_xp.set_xlim(xmin,xmax)
    hist_xp.set_ylim(ymin,ymax)
    hist_xp.set_xlabel("Nombre d'XP Thème 3")
    hist_xp.set_ylabel("Nombre d'élèves")
    hist_xp.set_title("Répartition des élèves selon leur nombre d'XP au thème 3")
    
    plt.show()
    stop()
    
def theme4():    
    L4 = [row[3] for row in T]
    xmin = 0
    xmax = 80
    ymin=0
    ymax=20
    
    fig, hist_xp = plt.subplots()
    
    plt.hist(L4)
    hist_xp.set_xlim(xmin,xmax)
    hist_xp.set_ylim(ymin,ymax)
    hist_xp.set_xlabel("Nombre d'XP Thème 4")
    hist_xp.set_ylabel("Nombre d'élèves")
    hist_xp.set_title("Répartition des élèves selon leur nombre d'XP au thème 4")
    
    plt.show()
    stop()
"""

def theme(): #Fonction regroupant les 4 en optimisant ! :D
    L = [0,1,2,3]
    xmin = 0
    XMAX = [55,100,100,80] #Choix des axes. Différents en fonction du zoom souhaité pour chaque histo.
    ymin = 0
    YMAX = [25,20,25,20]
    for i in L :
        L1 = [row[i] for row in T]
        xmax = XMAX[i]
        ymax = YMAX[i]
        
        fig, hist_xp = plt.subplots()
        
        plt.hist(L1)
        hist_xp.set_xlim(xmin,xmax)
        hist_xp.set_ylim(ymin,ymax)
        hist_xp.set_xlabel("Nombre d'XP du thème")
        hist_xp.set_ylabel("Nombre d'élèves")
        hist_xp.set_title("Répartition des élèves selon leur nombre d'XP du thème")
        
        plt.show()
        
        i+=1
        stop()
