#!/usr/bin/python
#################################
# DEPENDENCIAS
#import sys
import os
#from os import listdir
#################################

#Clase
class C_ManejoFicheros():
	x_ruta = "" #Ruta original de los archivos
	x_fichero = "" #Fichero sobre el que se actua
	x_almacen= "/home/victor/almacen" #Ruta a la que se copian los ficheros
	def imprimir(self):
		print x_ruta 

	def ejecutar(self):
		os.system('mplayer '+"'"+self.x_ruta+self.x_fichero+"'")

	def borrar(self):
		print "BORRANDO" 	
		os.system('rm '+"'"+self.x_ruta+self.x_fichero+"'")

	def copiar(self):
		print "COPIANDO"
		os.system('mv '+"'"+self.x_ruta+self.x_fichero+"' '"+self.x_almacen+"'")
