""" 
list (Array)
son colecciones o conjutno de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico 
Nota: Sus valores si son modificables

La lista es una coleccion ordenada y modificable. Permite miembros duplicados.
"""

import os
os.system("cls")

#Funciones mas comunes en las listas 
paises=["Mexico","España","Brasil","Canada"]
numeros=[23,45,8,24]
varios=["hola",3.1416,33,True]


#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)


#Recorrer la lista
#Primer forma 
for i in paises:
    print(i)
#Segunda forma
for i in range(0,len(paises)):
    print(paises[i])
#Tercera 
lista=""
for i in range(0,len(paises)):
    lista+=lista+f"[{paises[i]}],"
print(lista)


#Ordenar elementos de una lista
paises.sort()
print(paises)
numeros.sort()
print(numeros)
'''
no se puede comparar una cadena con un boleano "una persona con un auto"
varios.sort() 
print(varios) 
'''

#Dar la vuelta a una lista
paises.reverse()
print(paises)
varios.reverse()
print(varios)

#Agregar, insertar, Añadir un elemento a una lista
#Primer forma
paises.append("Honduras")
print(paises)
#Segunda forma
paises.insert(1,"Honduras")
print(paises)

#Ordenada alfabeticamente
paises.sort()
print(paises)

#Eliminar, borrar, suprimir un elemento de una lista
#Primer forma
paises.pop(4)
print(paises)
#Segunda forma
paises.remove("Honduras") #Cuando hay dos iguales nomas se borra una(la primera que encuentre)
print(paises)

#Buscar un elemento dentro de la lista
print(paises)
#Tiene que estar escrito igual
resp="Brasil" in paises 
print(resp)
#print("Brasil" in paises)


#Contar el numero de veces que aparece un elemento dentro de una lista
print(numeros)

numeros.append(23)
cuantos=numeros.count(23)
print(cuantos)


#Conocer la posicion o indice en que se encuentra un elemento de a lista
paises.reverse()
print(paises)
posicion=paises.index("Canada") #como buscar un nombre 
print(f"El valor de Canada lo encontro el la posicion: {posicion}")


#Unir el contenido de una lista dentro de otra
print(numeros)
numeros2=[100,200]

#crear a partir de la lista de numeros 1 y 2 un resultante y mostrar el contenido ordenado descendentemente

numeros.extend(numeros2)
print(numeros)
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)



