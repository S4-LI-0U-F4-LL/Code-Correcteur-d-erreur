//la fonction converti en binaire un mot donner en entrer

def conver(mot):

      liste = []
      i=0
          
      for char in mot:
               liste.append(str('0' + bin(ord(char))[2:])) 
      return  liste

//Affche mot (mot n, int i). Affcher les n bits de poids faible du mot x.





def affiche(mot,n):
      
      mots_bin=conver(mot)
      mots_bin.reverse()

      
      liste="".join(mots_bin)
      liste
      i = 0
      mot_n_bit=[]
      
      while i < n:
            
            
            mot_n_bit.append(liste[i])
            i = i+1

      
      return "".join(mot_n_bit)






// fonction qui retourne le poids du mot x.

def poid(mot):
      
      
      return mot.count("1")





// écrire une fonction de codage pour le code à répétition de longueur 3.

def repete(mot):
      
      liste=[]
      i=0
      while i < len(mot):
            if mot[i]=='1':
                  liste.append('111')
            else:
                  liste.append('000')
            i=i+1

      
      return "".join(liste)

            

m=affiche("bonjour",50)


