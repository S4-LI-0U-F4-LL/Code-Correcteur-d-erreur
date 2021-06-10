#code 
c=['0111','0101','1000','1001','1010','1000','1111','1011']

#calcul de poid

def poid(m):
	return m.count("1")

# recherche des coefficient du polynome enumerateur de polynome
def coefficient():

	coef=[]
	
	n=len(c[0])
	j=1
	
	
	
	while j<=n :
        
		i=0
		k=0
		while k < len(c):

			if(poid(c[k])==j):
				i=i+1
				
			k=k+1
		
		coef.append(i)
		j=j+1
	
			
	
	
	return coef
# affichage du polynome
def affiche(liste):

        s=[]
        s.append('1')
        i=1

        while i <=len(liste):
                
                s.append(str(liste[i-1])+"X^"+str(i))
                i=i+1
        
        
        return " + ".join(s)
        
        
#le p generer
p=affiche(coefficient())















           
