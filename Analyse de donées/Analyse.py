# -*- coding: utf-8 -*-
#A faire : moyenne de chaque gens

############################################################################################################################
#%% importation de module pour realiser le projet ##########################################################################
############################################################################################################################ 
import csv
import numpy as np
import sys
print("Bonjour! Bienvenue sur notre plateforme interactive !")
a = str(input("Pour bien commencer, veuillez cliquer sur 'p' si vous connaissez déjà les fonctions existentes, sinon tapez 'o' :"))
if a == "q" :
    sys.exit(0) 
else : 
    print("blablabla")

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

def maj(T,o,n):
    for i in range (len(T)): #pour tous les i appartenant Ã  l'intervalle [nombre d'Ã©lÃ©ments du tableau T]
    #si l'Ã©lÃ©ment est supÃ©rieur Ã  50, alors cet Ã©lÃ©ment prend comme valeur 50   
        if T[i,n] > o[n] : 
            T[i,n]= o[n] 
    return T

        
def maj_tout(T,o):
    n=0
    while n<len(o):
        T=maj(T,o,n)
        n+=1
    return T

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
name = input("Entrez le nom de l'eleve dont vous voulez connaitre les notes : \n") #Association d'un eleve a ses notes d'UE. Merci Philippe :)
rang = -1
if name in P:
    rang = P.index(name)
    print(name,"a obtenu les notes",T[rang]) #Enlever la derniere colonne et ajouter des lignes pour savoir si l'eleve a valide son UE
else:
    print("Vous ne connaissez pas vos eleves ? :( Entrez le nom d'un de vos eleves")
 """   
    
 
def nametorang(name):
    if name in P:
        return P.index(name)
    else:
        return "Erreur"


 
def fiche_eleve(name,T,c):
    if nametorang(name) != "Erreur":
        rang = nametorang(name)
        moyenne = moy_eleve(name,T,c)
        print(name, rang, " : Les notes de cette eleve sont ",T[rang],", sa moyenne est de ",moyenne)
    else:
        print("Erreur")
    
    
    
def oui_ou_non(name,T):
    if nametorang(name) != "Erreur":
        rang = nametorang(name)
        if T[rang,4] == 1.0:
            print(name," a bien eu son semestre !")
        else :
            print(name," n'a pas eu son semestre, et doit passer les rattrapages ...")
    else:
        print("Erreur")
    
    
    
#pas fini
def qui(P,T):
    for i in (len(T) and len(P)):
        T[i] = P(i)
        print(T)
            

#pas fini
def oui_ou_non_tous(T):
    d = 0
    for i in range (len(T)):
        if T[i,4] == 1.0 :
            d = nametorang(name)
            
            print(name, rang)
    

############################################################################################################################
#%% Attribution de chaque ligne de notes a un eleve ########################################################################
############################################################################################################################
#moyennes = np.mean(T,0)[:4] #0 : Traitement des valeurs en ligne pour chaque colonne.
                                    #Garde les 4 premieres valeurs

    

############################################################################################################################
#%% Moyenne pour un theme colonne n ########################################################################################
############################################################################################################################
def moy_colonne(n):
    moy = np.mean(T,0)[n]
    print(moy)
    
    
############################################################################################################################   
#%% Moyenne de chaque eleve ################################################################################################
############################################################################################################################ 
def moy_eleve(name,T,c):  #e : numéro de ligne du tableau et c : Coefficient ici 9
    m=0
    if nametorang(name) != "Erreur":
        rang = nametorang(name)
    else:
        print("Erreur")
    for i in range(len(T[rang])):
        m += T[rang][i]  #rang i dans la liste e (ligne du tableau) de la liste T
    m = m/c #On considère qu'une note sur 50 a un coefficient 1 dans notre cas actuel
    return m





