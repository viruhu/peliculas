#!/usr/bin/python
#################################
# DEPENDENCIAS
import sys
import os
#from os import listdir
#################################
param = sys.argv[1]
infile = open('/tmp/vv_tmp1.txt', 'r')
outfile = open('listado.txt', 'a')
print "PARAMETRO DE BUSQUEDA: "+param+"\n"
for x in range(1, 2):
	l_x=str(x)
	server = "https://www.youtube.com/results?search_query="
	search = param+"&page="+l_x

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




