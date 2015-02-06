#!/usr/bin/python
import sys
import os
from os import listdir

if len(sys.argv) == 1:
	print "se necesita un argumento"
	exit()

ruta=sys.argv[1]

for fichero in listdir(ruta):
	os.system('mplayer '+"'"+ruta+fichero+"'")
#	print "'B' Borrar, 'C' Copiar"
#	comando = raw_input()

