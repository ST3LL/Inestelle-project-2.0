#A faire : Donner des noms à chaque ligne + moyenne chaque UE + moyenne de chaque gens


#importation de module pour réaliser le projet 
import csv
import numpy as np

#récupération des données (le tableau) se trouvant sur le fichier "donnees_projet.txt"
with open('donnees_projet', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

entete = your_list.pop(0) #supprime la première ligne d'entête du tableau
T = np.array(your_list).astype(np.float) #transforme tous les éléments du tableau (string) en float


#Programme permettant de mettre les notes supérieures au plafond 
for i in range (len(T)): #pour tous les i appartenant à l'intervalle [nombre d'éléments du tableau T]
#si l'élément est supérieur à 50, alors cet élément prend comme valeur 50   
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
        
print(T)   


#Attribution de chaque ligne de notes à un élève 
P = ["Jean","Pierre","Michel","André","Philippe","René","Louis","Alain",\
     "Jacques","Bernard","Marcel","Daniel","Roger","Robert","Claude","Paul",\
     "Christian","Henri","Georges","Nicolas","François","Patrick","Gérard",\
     "Christophe","Joseph","Julien","Maurice","Laurent","Frédéric","David",\
     "Stéphane","Pascal","Sébastien","Alexandre","Thierry","Olivier","Thomas",\
     "Raymond","Antoine","Guy","Dominique","Charles","Didier","Marc","Vincent",\
     "Yves","Guillaume","Bruno","Serge","Maxime","Marie","Jeanne","Claude",\
     "Françoise","Monique","Catherine","Nathalie","Isabelle","Jacqueline",\
     "Anne","Sylvie","Martine","Madeleine","Nicole","Suzanne","Hélène",\
     "Christine","Marguerite","Denise","Christiane","Yvonne","Louise",\
     "Valérie","Sophie","Dominique","Sandrine","Stéphanie","Céline",\
     "Véronique","Chantal","Marcelle","Renée","Simone","Jeannine","Paulette",\
     "Julie","Annie","Patricia","Brigitte","Lucie","Camille","Léa","Alice",\
     "Aurélie","Laurence","Michèle","Cécile","Thérèse","Colette","Virginie"]

L = P.index(i)
N = T[i,:]


#Programme pour connaître le major d'une UE (non fini, problème dedans)
"""def fonct_major(T):
    for i in range(len(T)):
        temp=T[i]
        j=i
        while j>0 and temp<T[j-1]:
            T[j]=T[j-1]
            j-=1
        T[j]=temp
    return T""" 