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


infile = open('/tmp/vv_tmp1.txt', 'r')
outfile = open('listado.txt', 'a')
for x in range(1, 2):
	l_x=str(x)
	server = "https://www.youtube.com/results?search_query="
	search = "openerp+permisos"+"&page="+l_x

	os.system('wget "'+server+search+'" -O /tmp/vv_tmp'+l_x+'.txt')

	for line in infile:
		if line.find('watch?') != -1:
			ind = line.find('watch')
			link_f = line[ind:ind+19] 
			link="https://www.youtube.com/"+link_f
			outfile.write(link+"\n")

infile.close()
outfile.close()

f = open('listado.txt', 'r')
l = f.readlines()
s = set(l)

outfile = open('listado.txt', 'w')
outfile.writelines(s)
outfile.close()

os.system('youtube-dl -a listado.txt')




