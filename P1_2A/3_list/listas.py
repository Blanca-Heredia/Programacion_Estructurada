#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
import os
os.system("cls")

print("Lista de numeros: ")
lista_num=[1,2,3,4,5,6,7,8,9,10]
for i in lista_num:
    print(i)

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
os.system("clear")
lista_palabras=["hola","2023","Lebroncito","UTD","True","UTD"]
print(lista_palabras)
palabra_buscar=input("Dame la palabra a buscar: ")

if palabra_buscar in lista_palabras:
    print("SI se encontro la palabra en la lista")
else:
   print("NO se encontro la palabra en la lista")


#Ejemplo 3 Añadir elementos a la lista
lista_numeros=[]
opc="si"
while opc=="si":
    lista_numeros.append(float(input("Dame un numero entero o decimal: ")))
    opc=input("¿Desear agregar otro numero a las lista (si/no)? ").lower()
print(lista_numeros)   

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
        ["Marlene Heredia","6181234567"],
        ["Gustavo Heredia","6671234567"],
        ["Veronica Nuñez","6785678923"]
       ]

print(agenda)

for i in agenda:
    print(i)

for r in range(0,3):
    for c in range(0,2):
        print(agenda[r][c])    

cadena=""
for r in range(0,3):
    for c in range(0,2):
      cadena+=f"{agenda[r][c]}, "
    cadena+="\n"     
print(cadena) 