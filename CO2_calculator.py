#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import division
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import sys

#----------------------------------------------------------#
#-Calculadora de CO​2​ capturado por una parcela de árboles--#
#-------------Por:Jhoan Camilo Eusse Duque-----------------#
#--------------------------2016----------------------------#
#----------------------------------------------------------#

print "_"*60
 
print """Este programa permite determinar  la cantidad de
CO2 que almacena una parcela de árboles y ver la capacidad 
de almacenamiento individual de cada planta. Lo anterior 
se hará guiado bajo el Protocolo para la  estimación nacional 
y subnacional de biomasa-carbono en Colombia (MAVDT, IDEAM; 2011)
"""
print "_"*60


##Bloque 1. opción de usuario##


print """Por favor elija la zona de vida:
1. Bosque húmedo montano       bH-M 
2. Bosque húmedo montano bajo: bh-MB 
3. Bosque húmedo premontoano   bh-PM  
4. Bosque húmedo tropical      bh-T  
5. Bosque pluvial tropical     bp-T
6. Bosque seco tropical        bs-T """

user_option=int(input("Ingrese el número de la opción deseada: "))

if user_option == 1 :
	a= -2.45
elif user_option == 2 :
	a= -1.993
elif user_option == 3 :
	a= -2.289
elif user_option == 4 :
	a= -2.218
elif user_option == 5 :
	a= -2.413
elif user_option == 6 :
	a= -2.29
else :
	sys.exit("La opción que eligió no es válida, por favor elija una opción válida.") 



##Bloque 2. Ingreso de variables##

b=0.932

print "_"*60

print"""Tiene dos opciones para ingresar los datos necesarios:
1. Ingresar manuelmente
2. Usar base de datos"""

user_option=int(input("Ingrese el número de la opción deseada: "))



if user_option == 1:

	total_arboles=int(raw_input("Ingrese el número total de árboles de la parcela: "))
	
	CAP=([])
	altura=([])
	densidad=([])


	for i in xrange(total_arboles) :
		
		CAP=np.append(CAP, (float(input("Ingrese la circunferencia para el %d árbol (en cm) : "%(i+1))) / np.pi))
		altura=np.append(altura, (float(input("Ingrese la altura para el %d árbol (en m)          : "%(i+1)))))
        	densidad=np.append(densidad, (float(input("Ingrese la densidad para el %d árbol (en gm/cm3)   : "%(i+1)))))
	

elif user_option == 2:

	print"""Para crear una base de datos con Microsoft Excel que sea 
compatible con este programa,debe guardar el archivo 
como texto separado por tabulaciones (.txt) o texto 
con formato separado por espacios (.prn)."""

	ruta= raw_input("Ingrese la ruta de la base de datos: ")
	CAP, altura, densidad  = np.loadtxt(ruta,usecols=[0,1,2], unpack=True)
	
	total_arboles=len(CAP)

else:
	sys.exit("La opción que eligió no es válida, por favor elija una opción válida.")
	
DAP= CAP / np.pi

##Bloque 3.  Cálculos##

BA= np.exp(a + b*np.log((DAP**2)*altura*densidad))
BAT= np.sum(BA)/1000
CO2= (BA/1000) * 0.5 * 3.67
CO2T=BAT* 0.5 * 3.67


print "_"*60

print "Individuo N°      Biomasa Aerea(Kg)      CO2 capturado(Ton)"

print "_"*60

for i in xrange(total_arboles) :
	print "     %3d             %13.4f            %13.4f"%(i+1,BA[i],CO2[i]) 


print "_"*100

print "La parcela en total tiene una biomasa aérea de: %.5f Ton y captura en total: %.5f Ton de CO2"%(BAT,CO2T)


print "_"*100


##Bloque 4. Gráficas##

graphlab=np.zeros(len(BA))
x=np.arange(1,total_arboles+1,dtype=int)

plt.bar( x, BA, width=0.5, align='center', label='Biomasa aerea')
plt.bar( x + 0.25, CO2*1000, width=0.5, color='g', align='center', label='CO2 Capturado')
plt.bar(x, graphlab , label='CO2 total capturado: %.4f Ton'%(CO2T), color='r')
plt.title('Biomasa aerea y CO2 individual')
plt.xlabel('Individuo')
plt.ylabel('Kilogramos')
plt.legend(loc='center right', bbox_to_anchor=(1,1)) 


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(CAP, altura, CO2, rstride=10, cstride=10)
plt.title('CAP vs Altura vs CO2')
ax.set_xlabel('Circunferencia (en cm)')
ax.set_ylabel('Altura (en m)')
ax.set_zlabel('CO2 capturado (en Ton)')


plt.show()





