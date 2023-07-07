import numpy as np
import openpyxl

# Datos columna
base=0.35
altura=0.5
tension_carac=20.684
rec = .025

# Datos armadura
area= 4.91/10000
cant= [3,2,3]
pos= [0.035,0.25,0.465]
Fy = 551.58
diam_estribos = .006
diam_arm_esquinas = .025
diam_arm_bordes = .025
area_arm_esquinas = np.pi*diam_arm_esquinas**2/4
area_arm_bordes = np.pi*diam_arm_bordes**2/4
posicion = [
			# Esquina
			{"x": rec + diam_estribos + diam_arm_esquinas/2,
			 "y": altura-rec-diam_estribos-diam_arm_esquinas/2,
			 "area": area_arm_esquinas},
			{"x": base - (rec + diam_estribos + diam_arm_esquinas/2),
			 "y": altura-rec-diam_estribos-diam_arm_esquinas/2,
			 "area": area_arm_esquinas},
			{"x": rec + diam_estribos + diam_arm_esquinas/2,
			 "y": rec+diam_estribos+diam_arm_esquinas/2,
			 "area": area_arm_esquinas},
			{"x": base - (rec + diam_estribos + diam_arm_esquinas/2),
			 "y": rec+diam_estribos+diam_arm_esquinas/2,
			 "area": area_arm_esquinas},
			# Bordes
			{"x": rec + diam_estribos + diam_arm_esquinas/2,
			 "y": altura/2,
			 "area": area_arm_bordes},
			{"x": base - (rec + diam_estribos + diam_arm_esquinas/2),
			 "y": altura/2,
			 "area": area_arm_bordes},
			 ]

#for i in posicion:
#    print(i[0])
    #print(f"x={"x"} - y={y} - area={area}")

def coef_reduccion(Es):
    if Es < 0.002:
        coef = 0.65
    elif Es < 0.005:
        coef = 0.65+(Es-0.002)*(250/3)
    else:
        coef = 0.90
    return coef