# Datos columna
import numpy as np

base=0.35
altura=0.5
tension_carac=25

# Datos armadura
area= 4.91/10000
cant= [3,2,3]
pos= [0.035,0.25,0.465]

# Constantes
beta1= 0.85
ModYoung= 200000
Ecu=-0.003

# Calculo
phi= 0.00713

c=-Ecu/phi

armadura= []
Pn=-0.85*tension_carac*beta1*c*base
Mn=-0.85*tension_carac*beta1*c*base*(beta1*c-altura)/2

for i in range(len(pos)):
	Esi= phi*(pos[i]-c)
	if np.abs(Esi*ModYoung) < 420: 
		fsi= Esi*ModYoung
	elif Esi*ModYoung < 0:
		fsi= -420
	else:
		fsi=420
	
	disty= pos[i]-altura*0.5
	armadura.append([area*fsi*cant[i],disty])

	Pn+= area*fsi*cant[i]
	Mn+= area*fsi*cant[i]*disty
	print(area*fsi*cant[i])

e=-Mn/Pn	
print(Pn, Mn, e)