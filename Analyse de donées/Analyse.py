# -*- coding: utf-8 -*-
#A faire : moyenne de chaque gens

############################################################################################################################
#%% importation de module pour realiser le projet ##########################################################################
############################################################################################################################ 
import csv
import numpy as np
import sys
import matplotlib as plt


def stop():
    a=str(input("Souhaitez-vous continuer ? Oui : o, Non : n"))
    if a == "o" :
        pass
    else : 
        sys.exit(0) 


print("Bonjour! Bienvenue sur notre plateforme interactive !")
a = str(input("Pour bien commencer, veuillez cliquer sur 'p' si vous ne connaissez pas les fonctions existantes, sinon tapez 'c' :"))
if a == "c" :
    pass
elif a == "P" :
    print ("Voici les fonctions existantes : blabla")
stop()



############################################################################################################################
#%% Programme permettant de mettre les notes superieures au plafond ########################################################
############################################################################################################################
with open('donnees_projet', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

entete = your_list.pop(0) #supprime la premiere ligne d'entete du tableau
T = np.array(your_list).astype(np.float) #transforme tous les elements du tableau (string) en float


############################################################################################################################
#%% Programme permettant de mettre les notes superieures au plafond ########################################################
############################################################################################################################
"""
for i in range (len(T)): #pour tous les i appartenant aÂ  l'intervalle [nombre d'elements du tableau T]
#si l'element est superieur aÂ  50, alors cet element prend comme valeur 50   
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

maxs = [50,100,100,200]


def maj(T,o,n):
    for i in range (len(T)): #pour tous les i appartenant à  l'intervalle [nombre d'éléments du tableau T]
    #si l'élément est supérieur à  50, alors cet élément prend comme valeur 50   
        if T[i,n] > o[n] : 
            T[i,n]= o[n] 
    return T
    stop()
    

    
def maj_tout(T,o):
    n=0
    while n<len(o):
        T=maj(T,o,n)
        n+=1
    return T
    stop()

############################################################################################################################
#%% fonction permettant de terminer le major de chaque theme ###############################################################
############################################################################################################################
def major (l,n):
    a_trier = []
    for liste in l :
        a_trier.append([liste[n]])
    for i in range (len(a_trier)):
        a_trier[i].append(i)
    a_trier = sorted(a_trier)
    a_trier = a_trier[::-1]
    print(a_trier[1])
    stop()


############################################################################################################################
#%% Attribution de chaque ligne de notes a un eleve######################################################################### 
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
        return P.index(name)
    else:
        return "Erreur"
        
  
#pas fini
def qui(T,P):
    for i in range (len(T)):
        ihih = P[i]
        eheh = T.index(ihih)
    return eheh
            

 
def fiche_eleve(name,T,c):
    if nametorang(name) != "Erreur":
        rang = nametorang(name)
        moyenne = moy_eleve(name,T,c)
        print(name, rang, " : Les notes de cette eleve sont ",T[rang],", sa moyenne est de ",moyenne)
    else:
        print("Erreur")
    stop()
  
    
############################################################################################################################
#%% Quels élèves ont eu leur semestre ###################################################################################### 
############################################################################################################################     
    
def oui_ou_non(name,T):
    if nametorang(name) != "Erreur":
        rang = nametorang(name)
        if T[rang,4] == 1.0:
            return True
        else :
            return False
    else:
        return None
 

       
def print_oui_ou_non(name,T):
    if oui_ou_non(name,T) == True :
        print(name, "a eu son semestre !")
    elif oui_ou_non(name,T) == False :
        print(name,"n'a pas eu son semestre, et doit passer les rattrapages ...")
    else :
        print("Erreur")
    stop()



def oui_ou_non_tous(P,T):
    r = []
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
#%% Courbe nb XP <=> note sur 20 ###########################################################################################
############################################################################################################################ 

AA = [0,3,8,16,25,36,48,62,78,94,112,131,151,172,194,218,243,267,294,321,350]
BB = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

AAsur450 = [9/7*e for e in AA]



def indexmin(AAsur450,xp):
    i = 0
    while xp > T[int(AAsur450)] :
        i += 1
        # if i > len(AAsur450) : error
    return i - 1
#print(indexmin(AAsur450,23))


def arrondir(xp,n):
    # arrondi a n chifres apres la virgule...
    return int(xp*10**n)/10**n

#convertit le nombre d'XP en une note sur 20 arrondi à 2 chiffres après la virgule
def note(xp,AAsur450):
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


#affiche la courbe pallier/note sur 20
def courbe_nbXP_note20(plafond): 
    x = np.linspace(0,plafond+30,10)
    plt.plot(AA,BB,"+")
    plt.ylabel('Nombre de XP')
    plt.xlabel("Note sur 20")
    plt.show()

tabsommexp = [sum(c[:-1]) for c in maj_tout(T,maxs)]
notes = [note(xp,AAsur450) for xp in tabsommexp]


#affiche un graphique avec un nuage de points (élèves ayant au dessus de la moyenne et en dessous)
def notes_sur_20():
    tabsommexp = [sum(c[:-1]) for c in maj_tout(T,maxs)]
    notes = [note(xp,AAsur450) for xp in tabsommexp]
    notes.sort()
    plt.plot([0,100],[10,10],'-')
    plt.plot(range(len(notes)),notes,'+')
    plt.show() 
 
    
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
#%% Affiche un camembert des élèves au-dessus de la moyenne et en dessous  #################################################
############################################################################################################################
def camembertNotes():
    labels = 'Supérieur à 10', 'Inférieur à 10'
    sizes = [90,10] #90% des élèves ont au dessus de 10 et 10% en dessous.
    explode = (0, 0.3)  # Met en exergue les 10% en dessous de la moyenne
    
    fig, camembert = plt.subplots()
    camembert.pie(sizes, labels=labels, explode=explode, shadow=True)
    camembert.axis('equal') #Permet d'avoir un beau camembert circulaire. =D

    plt.show()

############################################################################################################################   
#%% Histogramme répartition élèves selon nombre d'XP dans chaque thème  ####################################################
############################################################################################################################ 
def theme1():    
    L1 = [row[0] for row in T] #Récupère la première colonne de T dans la liste L1 correspondant aux notes du 1er thème
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
    
    
def theme4():    
    L4 = [row[3] for row in T]
    xmin = 0
    xmax = 200
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


