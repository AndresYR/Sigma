import numpy as np
import xlwings as xw
import utils

# Conexion con Excel
xw.Book("columnasHA.xlsm").set_mock_caller()
wb = xw.Book.caller()
sheet = wb.sheets[0]

# Datos columna
base=sheet["H2"].value/100
altura=sheet["H3"].value/100
tension_carac=sheet["H4"].value/100
rec = sheet["H5"].value/100

# Datos armadura
barras_sup_e_inf = sheet["H8"].value
barras_laterales = sheet["H9"].value

diam_barras_esq = sheet["H10"].value/1000
area_barras_esq = np.pi*diam_barras_esq**2/4
area_barras_lat = 0
if barras_sup_e_inf or barras_laterales:
	diam_barras_otras = sheet["H11"].value/1000
	area_barras_otras = np.pi*diam_barras_otras**2/4
diam_estribos = sheet["H12"].value/1000

posicion = [
			# Esquina
            ## Sup Izq
			{"x": rec + diam_estribos + diam_barras_esq/2,
			 "y": altura-rec-diam_estribos-diam_barras_esq/2,
			 "area": area_barras_esq},
			## Sup Der
            {"x": base - (rec + diam_estribos + diam_barras_esq/2),
			 "y": altura-rec-diam_estribos - diam_barras_esq/2,
			 "area": area_barras_esq},
			## Inf Izq
            {"x": rec + diam_estribos + diam_barras_esq/2,
			 "y": rec+diam_estribos + diam_barras_esq/2,
			 "area": area_barras_esq},
			## Inf Der
            {"x": base - (rec + diam_estribos + diam_barras_esq/2),
			 "y": rec+diam_estribos + diam_barras_esq/2,
			 "area": area_barras_esq}
	]

for i in posicion:
	print(f"x: {i['x']} y: {i['y']} As: {i['area']}")

def pos_sup_inf(barras_sup_inf, posicion):
	if barras_sup_inf != 0:
		delta_x = (posicion[0]["x"]-posicion[1]["x"])/(barras_sup_inf+1)
		for x in range(barras_sup_inf):
			pass