import calificaciones

def main():
    datos = []
    opcion = ""

    while True:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregarCalificaciones(datos)
                calificaciones.espereTecla()
            case "2":
                calificaciones.mostrarCalificaciones(datos)
                calificaciones.espereTecla()
            case "3":
                calificaciones.calcularCalificaciones(datos)
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
