# -*- coding: utf-8 -*-

#Author: Angel Yocupicio
#Web: www.respirocodigo.com
#Python: 3.8.x
#Código para hacer análisis SEO en archivos de texto

print("<< Análisis SEO local >>")

logo = """
			vvvvv     vvvvvvvvvvvv     vvvvv
			 vvvvv   vvvvvvvvvvvvvv   vvvvv
			  vvvvv vvvvvvvvvvvvvvvv vvvvv
			   vvvvvvvvv        vvvvvvvvv
			    vvvvvvv          vvvvvvv
			     vvvvv            vvvvv
			    vvvvvvv          vvvvvvv
			   vvvvvvvvv        vvvvvvvvv
			  vvvvv vvvvvvvvvvvvvvvv vvvvv
			 vvvvv   vvvvvvvvvvvvvv   vvvvv
			vvvvv     vvvvvvvvvvvv     vvvvv"""
print(logo)
archive = str(input("Escribe el nombre y extensión del archivo: "))
numberkeys = int(input("¿Cuántas Keywords quieres analizar? "))

file = open("{}".format(archive),"r")
reading = file.read()
words = len(reading.split())

keywords = []
frecuency = []
seo = []

for k in range(numberkeys):
    keywords.append([0]*numberkeys)
    frecuency.append([0]*numberkeys)
    seo.append([0]*numberkeys)

for i in range(numberkeys):
    palabraclave = ("Dime la Keyword %d: " % (i+1))
    keywords[i] = str(input(palabraclave))
    frecuency[i] = reading.count(keywords[i])
    seo[i] = (frecuency[i]/float(words))*100

print("Se encontraron {} palabras en el archivo {}.".format(words,archive))

for j in range(numberkeys):
	print("La << Keyword {} = {} >> aparece {} veces. Su densidad es {}%.".format(j+1,keywords[j],frecuency[j],round(seo[j],2)))

file.close()
print("\n¡FIN del Código Python!")
