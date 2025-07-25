import ropa

opc = True

while opc == True:
    ropa.borrarPantalla()
    print("👖 SISTEMA DE INVENTARIO DE ROPA 👗\n")
    ropa.mostrar_menu()
    opcion = input("\n🔸 Opción: ")
    
    match opcion:
        case "1":
            ropa.agregar_prenda()
            ropa.espereTecla()
        case "2":
            ropa.ver_inventario()
            ropa.espereTecla()
        case "3": 
            ropa.eliminar_prenda()
            ropa.espereTecla() 
        case "4":
            print("\n👋 ¡Gracias por usar el sistema!")
            ropa.espereTecla() 
            opc = False  
        case _:
            print("\n⚠️ Opción inválida. Vuelve a intentar.")   
            ropa.espereTecla()
