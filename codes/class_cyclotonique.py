##cyclotonique
print("###########################################################################")
print("#####################                          ############################")
print("##################### UNIVERSITE GASTON BERGER ############################")
print("#####################   SAINT LOUIS SENEGAL    ############################")
print("#####################        UFR SAT           ############################")
print("#####################                          ############################")
print("###########################################################################")
print("\n\n")

print ("############################################################################")
print ("#####################                                  #####################")
print ("#####################      ALGEBRE ET APPLICATION      #####################")
print ("#####################      CODE CORRECTEUR ERREUR      #####################")
print ("#####################             SALIOU FALL          #####################")
print ("#####################                                  #####################")
print ("############################################################################")
print("\n\n")

print ("############################################################################")
print ("#####################          IMPLEMENTATION          #####################")
print ("#####################.             DES	               #####################")
print ("#####################             CLASS                #####################")
print ("#####################          CYCLOTONIQUE            #####################")
print ("############################################################################")

print('pour Tester la fonction :tapez la fonction class_cyclo(n) \n n un nombre premier')

def class_cyclo(n):
	a=[2**i for i in range(n)]
	j=1
	liste=[]
	k=0
	liste.append([0])
	while j<len(a):
		c=[]
		#print(liste)
		for i in range(0,len(a)):
			if test1(c,(j*a[i])%n)==False:
				c.append((j*a[i])%n)

		if test(liste,j) != True:
			liste.append(c)
		j=j+1
	return liste

def test(liste,j):
	for x in liste:
		for i in range(0,len(x)):
			if j == x[i]:
				return True



def test1(liste,j):
	return j in liste

