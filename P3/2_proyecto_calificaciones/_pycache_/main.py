import calificaciones

def main():
    datos = []
    opcion = ""

    while True:
        calificaciones.borrarPantalla()
        print("\n\t\t\t .::: GESTION DE CALIFICACIONES :::. \n\n\t 1.-Ingresar calificacion  \n\t 2.- Mostrar calificacion \n\t 3.- Calcular calificaiones \n\t 4.- Salir")
        opcion=input("\n\t\t Elige una opción: ").upper()
        

        match opcion:
            case "1":
                calificaciones.agregarCalificaciones()
                calificaciones.espereTecla()
            case "2":
                calificaciones.mostrarCalificaciones()
                calificaciones.espereTecla()
            case "3":
                calificaciones.calcularCalificaciones()
                calificaciones.espereTecla()
            case "4":
                calificaciones.borrarPantalla()
                print("✅  Terminaste la ejecución del sistema")
                break
            case _:
                print("❌  Opción inválida, vuelve a intentarlo")
                calificaciones.espereTecla()

if __name__ == "__main__":
    main()
