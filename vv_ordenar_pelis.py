#!/usr/bin/python
import sys
import os
from os import listdir
from mis_libs import C_ManejoFicheros


if len(sys.argv) == 1:
	print "se necesita un argumento"
	exit()

O_pelis = C_ManejoFicheros()
O_pelis.x_ruta = sys.argv[1]

for fichero in sorted(listdir(O_pelis.x_ruta)):
	os.system('clear')
	print fichero
	O_pelis.x_fichero = fichero
	O_pelis.ejecutar()
	
	comando = raw_input("'B' Borrar, 'G' Guardar \n")
	comando=comando.upper()

	if comando == "B":
		O_pelis.borrar()
	elif comando== "G":
		O_pelis.copiar()
	else:
		print "NO HACER NADA"

	comando = raw_input("Pulsa una techa para continuar...")

