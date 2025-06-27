calificaciones={}

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("Oprima cualquier tecla para continuar")

def menu_principal():
    print("GESTION DE CALIFICACIONES 1.Agregar 2.Mostrar 3.Calcular promedios 4.Salir") 
    opcion=input("Elige una opcion:").upper()
    return opcion

def agregarCalificaciones(lista):
    borrarPantalla()
    print("Agregar calificaciones")
    nombre=input("Nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input("Ingresa la calificacion #{i}: "))
                if cal>=0 and cal<=10:
                   calificaciones.append(cal)
                   continua=False
                else:
                 print("La calificacion debe estar entre 0 y 10")
               
            except ValueError:
              print("Ingresa un valor numerico")
    lista.append({nombre}+calificaciones)
    print("¡LA OPERACION SE REALIZO CON EXITO!")

def mostrarCalificaciones(lista):
    borrarPantalla()
    print("Mostrar TODAS las calificaciones")
    if len(lista)>0:
        print(f"{'Nombre':<15}  {'Calificacion 1':<10}  {'Calificacion 2':<10}  {'Calificacion 3':<10}")
        print("-"*60)
        for fila in lista:
            print(f"{fila[0]:<15}  {fila[1]:<10}  {fila[2]:<10}  {fila[3]:<10}")
        print("-"*60)
        cuantos=len(lista)
        print(f"Son {cuantos} alumnos")
    else:
        print("No hay calificaciones en el sistema")

def calcularCalificaciones(lista):
    borrarPantalla()
    print("Promedios de los alumnos")
    if len(lista)>0:
        print(f"{'Nombre':<15}  {'Calificacion 1':<10}  {'Calificacion 2':<10}  {'Calificacion 3':<10}")
        print("-"*40)
        promedio_grupal=0
        for fila in lista:
            nombre=fila[0]
            #promedio=(fila[1]+fila[2]+fila[3])/3
            promedio=sum(fila[1:])/3
            print(f"{nombre:<15}{promedio_grupal:.2f}")
            promedio_grupal+=promedio
            print("-"*40)
        promedio_grupal=promedio_grupal/len(lista)
        print(f"El promedio del grupo es: {promedio_grupal:.2f}")
    else:
        print("No hay calificaciones en el sistema")

