inventario = []

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("🛑 Oprima cualquier tecla para continuar")

def mostrar_menu():
    borrarPantalla()
    print("\n\t🛍️ --- TIENDA DE ROPA ---")
    print("\n\t1️⃣  Agregar prenda")
    print("\n\t2️⃣  Ver inventario")
    print("\n\t3️⃣  Eliminar prenda")
    print("\n\t4️⃣  Salir")

def agregar_prenda():
    borrarPantalla()
    print("\n\t➕ AGREGAR PRENDA")
    
    nombre = input("🏷️ Marca: ").upper().strip()
    tipo = input("👕 Tipo (camisa, pantalón, etc.): ").upper().strip()
    talla = input("📏 Talla (S, M, L, XL, etc.): ").upper().strip()
    
    while True:
        try:
            precio = float(input("💰 Precio: "))
            break
        except ValueError:
            print("❌ Solo se aceptan números. Intenta de nuevo.")
    
    color = input("🎨 Color: ").upper().strip()
        
    prenda = {
            'nombre': nombre,
            'tipo': tipo,
            'talla': talla,
            'precio': precio,
            'color': color
    }
    
    inventario.append(prenda)
    print(f"\n\t✅ '{nombre}' agregada correctamente!")

def ver_inventario():
    borrarPantalla()
    print("\n\t📦 INVENTARIO:")

    if len(inventario) > 0:
        print(f"{'🏷️ Marca':<15}{'👕 Tipo':<10}{'📏 Talla':<10}{'💰 Precio':<10}{'🎨 Color':<10}")
        print("-"*50)
        for prenda in inventario:
            print(f"{prenda['nombre']:<15}{prenda['tipo']:<10}{prenda['talla']:<10}{prenda['precio']:<10}{prenda['color']:<10}")
        print("-"*50)
        cuantos = len(inventario)
        print(f"\n\t🧾 Son {cuantos} prendas")
    else:
        print("\n\t🚫 No hay ropa en el inventario") 

def eliminar_prenda():
    borrarPantalla()
    print("\n\t🗑️ Eliminar alguna prenda ")
    ver_inventario() 

    if not inventario:
        return
    
    try:
        num = int(input("\n🔢 Número de prenda a eliminar: ")) - 1
        if 0 <= num < len(inventario):
            eliminada = inventario.pop(num)
            print(f"✅ '{eliminada['nombre']}' eliminada.")
        else:
            print("\n❌ Número inválido.")
    except ValueError:
        print("\n⚠️ Debes ingresar un número.")
