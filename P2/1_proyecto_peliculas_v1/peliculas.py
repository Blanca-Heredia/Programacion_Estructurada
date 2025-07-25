#Dict u objeto que permita almacenar los siguientea atributos (nombre, categoria, clasificacion, genero, idioma) de peliculas 


#pelicula={
#    "nombre":"",
 #  "clasificacion":"",
#  "genero":"",
#   "idioma":""
#}

peliculas={}

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
                print("La pelicula que se borro ")

def crearPeliculas():
    borrarPantalla()
    print("Agregar peliculas")
    peliculas.update({"Nombre":input("Ingresa el nombre: ").upper().strip()})
   # peliculas["nombre"]=input("Ingrese el nombre: ").upper().strip()
    peliculas.update({"Categoria":input("Ingresa la categoria: ").upper().strip()})
    peliculas.update({"Clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
    peliculas.update({"Genero":input("Ingresa el genero: ").upper().strip()})
    peliculas.update({"Idioma":input("Ingresa el idioma: ").upper().strip()})
    print("LA OPERACION SE REALIZO CON EXITO")

def mostrarPeliculas():
    borrarPantalla()
    print("Mostrar las peliculas")
    if len(peliculas)>0:
        for i in peliculas:
            print(f"{i+1} : {peliculas[i]}")
        else:
            print("No hay peliculas")

def borrarPeliculas():
    borrarPantalla()
    print("Borrar peliculas")
    print("Mostrar las peliculas")
    if len(peliculas)>0:
        resp=input("Desear quitar la peliculas? (Si/No)").lower().strip()
        if resp=="si":
            peliculas.clear()
    else:
        print("No hay peliculas")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("Agregar caracteristica ")
    cambio=(input("Escribe la caracteristica a cambiar: ")).strip().lower()
    valor=(input("Escribe la caracteristica nueva")).strip().upper()
    peliculas.update({cambio:valor})
    print("¡LA OPERACION SE REALIZO CON EXITO!")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("Modificar características de la película")
    if len(peliculas)>0:
        for i in peliculas:
            print(f"{i}:{peliculas[i]}")
            resp = input(f"¿Deseas modificar el valor de la caracteristica {i}? (Si/No): ").lower().strip()
            if resp == "si":
                valor=input(f"Introduce el nuevo valor para {i}: ").upper().strip()
                #peliculas.uppdate({i:valor})
                peliculas[i]=valor
                print("¡LA OPERACION SE REALIZO CON EXITO!")

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("Borrar caracteristica de peliculas")
    print("Valores actuales")
    print(f"{i} : {peliculas[i]}") 
    if len(peliculas)>0:
        for i in peliculas:    
            resp=print("Deseas borra alguna caracteristica? (Si/No):").upper().strip()
            if resp=="si":
                print("Ingresa la caracteristica que deseas borrar: ")



           