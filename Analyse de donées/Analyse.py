#A faire : moyenne chaque UE + moyenne de chaque gens


#importation de module pour realiser le projet 
import csv
import numpy as np

#recuperation des donnees (le tableau) se trouvant sur le fichier "donnees_projet.txt"
with open('donnees_projet', 'r') as f:
    reader = csv.reader(f)
    your_list = list(reader)

entete = your_list.pop(0) #supprime la premiere ligne d'entete du tableau
T = np.array(your_list).astype(np.float) #transforme tous les elements du tableau (string) en float


#Programme permettant de mettre les notes superieures au plafond 
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


#Attribution de chaque ligne de notes a un eleve
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


name = input("entrez un nom \n") #Association d'un eleve a ses notes d'UE. Merci Philippe :)
rang = -1
try:
    rang = P.index(name)
    print(T[rang])
except:
    print("erreur : pas connu")

#Moyenne de chaque UE (moyenne de chaque colonne)
moy_colonne = np.mean(T,0)[:4] #0 : Traitement des valeurs en ligne pour chaque colonne.
                                    #Garde les 4 premieres valeurs

#





#Programme pour connaitre le major d'une UE (non fini, probleme dedans)
"""def fonct_major(T):
    for i in range(len(T)):
        temp=T[i]
        j=i
        while j>0 and temp<T[j-1]:
            T[j]=T[j-1]
            j-=1
        T[j]=temp
    return T""" 