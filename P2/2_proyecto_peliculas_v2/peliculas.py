peliculas=[]

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("Oprima cualquier tecla para continuar")

def agregarPeliculas():
    borrarPantalla()
    print("Agregar peliculas")

    peliculas.append(input("Ingresa el nombre: "))
    print("¡LA OPERACION SE REALIZO CON EXITO!")

def mostrarPeliculas():
    borrarPantalla()
    print("Mostrar TODAS las peliculas")
    if len(peliculas)>0:
        for i in range(0, len(peliculas)):
            print(f"{i+1} : {peliculas[i]}")

    print("No hay peliculas en este momento")

def limpiarPeliculas():
    borrarPantalla()
    print("Limpiar o borrar TODAS las peliculas")
    resp=(input("Deseas borrar todas las peliculas del sistema? (Si/No) ")).lower().sript()
    if resp=="si":
        peliculas.clear()
        print("¡LA OPERACION SE REALIZO CON EXITO!")

def buscarPeliculas():
    borrarPantalla()
    print("Buscar peliculas")
    pelicula_buscar=input("Ingrese el nombre de las peliculas: ").upper().strip()
    if not (pelicula_buscar in peliculas):
     print("Esta peliculas a buscar no existe en el sistema")
    else:
        encontro=0
        for i in range(0, len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                print(f"La pelicula {pelicula_buscar} se encuentra en el casillero {i+1}")
                encontro+=1
        print(f"Tenemos {encontro} pelicula(s) con este titulo")
        print("¡LA OPERACION SE REALIZO CON EXITO!")

def modificarPeliculas():
    borrarPantalla()
    print("Modificar peliculas")
    peliculas_buscar=input("Ingresa la peliculas que quieres modificar").upper().strip()
    encontro=0
    if not (peliculas_buscar in peliculas):
        print("Esta peliculas a modificar no existe en el sistema")
    else:
        for i in range(0, len(peliculas)):
            if peliculas_buscar==peliculas[i]:
                resp=input("Deseas actualizar la peliculas? (Si/No)").lower()
                if resp=="si":
                  peliculas[i]=input("Introduce el nuevo nombre de la peliculas:").upper().strip()
                  encontro+=1
                  print("LA OPERACION SE REALIZO CON EXITO")

        print(f"Se modifico {encontro} con este titulo")

def borrarPeliculas():
    borrarPantalla()
    print("Borrar peliculas")
    peliculas_buscar=input("Escribe el nombre de la pelicula que quieres buscar: ")
    encontro=0
    for i in range(0, len(peliculas)):
        if peliculas_buscar==peliculas[i]:
             print(f"La pelicula {peliculas_buscar} se encuentra en el casillero {i+1}")
             encontro+=1
             resp=input("Deseas quitar o borrar la pelicula del sistema? (Si/No): ").lower()
             if resp=="si":
                peliculas.pop(i)
                print("La pelicula se borro ")

            
                



    