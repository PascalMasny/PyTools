#YT Tutorial
#https://www.youtube.com/watch?v=pvimAM_SLic

import random

f = open("pi.csv" , "w")

def schaetzung_pi(n):
	nr_punkte_im_kreis = 0
	nr_punkte_ges = 0

	for _ in range(n):

		#random nr 0-1
		x = random.uniform(0,1)
		y = random.uniform(0,1)

		f.write("pi," + str(x) + "," + str(y)+ "\n")
		
		#Abstand Berechnen
		abstand = x**2 + y **2
		
		#abstand abfragen und eintragen
		if abstand <= 1:
			nr_punkte_im_kreis += 1
		nr_punkte_ges += 1

	#return ergebniss
	return 4 * nr_punkte_im_kreis / nr_punkte_ges

#ausgabe
#mehr Punkte => Akurater
print(schaetzung_pi(100))