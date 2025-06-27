import calificaciones
def main():
    datos =[]
opcion=True
while opcion:
    calificaciones.borrarPantalla()
    calificaciones.menu_principal()

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
            opcion=False
            calificaciones.borrarPantalla()
            print("Terminaste la ejecucion del sistema")
        case _:
            opcion=True
            print("Opcion invalida, vuelva a intentarlo")

    if __name__=="__main__":
     main()






