""" 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.

"""


paises={"México","Brazil","España","Canada"}
print(paises)

varios={True,"UTD",33,3.14}
print(varios)

#Funciones u operaciones

paises.add("Mexico")
print(paises)
  
paises.pop()
print(paises)

paises.remove("Mexico")

#Ejemplo crear un programa que solicite los email de los alumnos de la  UTD almacenar
#  en una lista y posteriosmente mostrar en la pantalla los email sin duplicados


#Solucion 1
email={}
opc="si"
email={""}
while opc=="si":
    email=(input("Escribe el email del alumno: "))
    opc=input("¿Desear agregar otro email (si/no)? ")
print(email)   


import os
os.system("cls")

#Solucion 2
resp="si"
emails=[]
while resp=="si":
    emails.append(input("Escribe el email: "))
    resp=input("Quiere agregar otro email? ")
emails_set=set(emails)#QUITAR DUPLICADOS
print(emails_set)
emails=list(emails_set)
print(emails)

