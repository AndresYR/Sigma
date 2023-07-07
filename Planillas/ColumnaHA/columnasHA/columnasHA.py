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
recubrimiento = sheet["H5"]/100

# Datos armadura
barras_sup_e_inf = sheet["H8"].value
barras_laterales = sheet["H9"].value

diam_barras_esq = sheet["H10"].value/1000
area_barras_esq = np.pi*diam_barras_esq**2/4
if barras_sup_e_inf or barras_laterales:
	diam_barras_lat = sheet["H11"].value/1000
	area_barras_lat = np.pi*diam_barras_lat**2/4

area= 2.85/10000
cant= [4,2,2,4]
area_total = area*sum(cant)
pos= [0.06,0.1867,0.3133,0.44]
Fy = 413.69

# Constantes
beta1= 0.85
ModYoung= 200000
Ecu=-0.003


sheet[0,0].value = "Pn"
sheet[0,1].value = "Mn"
sheet[0,2].value = "e"
sheet[0,3].value = "c"
sheet[0,4].value = "coef red"


# Calculo
c_array= np.arange(altura+0.1, -altura/2,-0.01)
row = 0

for c in c_array:
	phi= -Ecu/c
	Pcompresion= -0.85*tension_carac*(beta1*c*base-area_total)
	Pn= Pcompresion
	Mcompresion= Pcompresion*(beta1*c-altura)/2
	Mn= Mcompresion
	Totaltraccion = 0
	TotalMomentoTraccion = 0
	Es=[]
	for i in range(len(pos)):
		Esi= phi*(pos[i]-c)
		Es.append(Esi)
		if np.abs(Esi*ModYoung) < Fy: 
			fsi= Esi*ModYoung
		elif Esi*ModYoung < 0:
			fsi= -Fy
		else:
			fsi= Fy
	
		disty= pos[i]-altura*0.5
		Ptraccion= area*fsi*cant[i]
		Pn+= Ptraccion
		Totaltraccion+=Ptraccion
		Mtraccion=area*fsi*cant[i]*disty
		Mn+= Mtraccion
		TotalMomentoTraccion += Mtraccion
		if Pn > 0:
			Pn= Totaltraccion
			Mn= TotalMomentoTraccion

	e=-Mn/Pn	
	

	coef_reduccion = utils.coef_reduccion(np.abs(np.max(Es)))
	P0 = -0.8*(0.85*tension_carac*(base*altura-area_total)+area_total*Fy)
	if np.abs(Pn*coef_reduccion) > np.abs(P0*.65):
		Pn = P0

	if Mn>=0 and c>0:
		row+= 1
		if row == 1:
			sheet[row,0].value = -P0*0.65
			sheet[row,1].value = 0
			sheet[row,2].value = 0
			sheet[row,3].value = 0
			sheet[row,4].value = 0.65
			
		else:
			print(f"| Pn= {round(Pn,4)} | Mn= {round(Mn,4)} | e= {round(e,3)} | c={round(c,2)}")
			sheet[row,0].value = -Pn*coef_reduccion
			sheet[row,1].value = Mn*coef_reduccion
			sheet[row,2].value = e
			sheet[row,3].value = c
			sheet[row,4].value = coef_reduccion
