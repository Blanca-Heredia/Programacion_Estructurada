#Crear un proyecto que permita gestionar (administrar) peliculas. Colocar un menu de opciones para agregar, Borrar, Modificar, Mostrar, Buscar, Limpiar una lista de peliculas 
#Notas 
#1.-Utilizar funciones y mandar llamar desde otro archivo
#2.-Utilizar listas para almacenar los nombres de peliculas 


import peliculas

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("GESTION DE PELICULAS 1.Agregar 2.Borrar 3.Modificar 4.Mostrar 5.Buscar 6.Limpiar 7.Salir") 
    opcion=input("Elige una opcion:").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.espereTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.espereTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.espereTecla()
        case "4":
            peliculas.mostrarPeliculas()
            peliculas.espereTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.espereTecla()
        case "6":
            peliculas.limpiarPeliculas()
            peliculas.espereTecla()
        case "7":
            opcion=False
            peliculas.borrarPantalla()
            print("Terminaste la ejecucion del sistema")
        case _:
            opcion=True
            print("Opcion invalida, vuelva a intentarlo")

            



