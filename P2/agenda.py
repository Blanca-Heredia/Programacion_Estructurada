def borrarPantalla():    
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("Presione una tecla para continuar...")

def menu_principal():
    borrarPantalla()
    print("📖 Sistema de gestión de Agenda de Contactos 📖")
    print(" 1. Agregar contacto")
    print(" 2. Mostrar todos los contactos")
    print(" 3. Buscar contacto por nombre")
    print(" 4. Modificar contacto")
    print(" 5. Eliminar contacto") 
    print(" 6. Salir")
    return input("👉 Seleccione una opción (1-6): ")

def agregar_contacto(agenda):
    borrarPantalla()
    print("📥 Agregar Contacto")
    nombre = input("Nombre: ").upper().strip()
    if nombre in agenda:
        print("⚠️ Este contacto ya existe")
    else:
        tel = input("Teléfono: ").strip()
        email = input("E-mail: ").strip().lower()
        agenda[nombre] = [tel, email]
        print("✅ Contacto agregado con éxito")

def mostrar_contacto(agenda):
    borrarPantalla()
    print("📋 Mostrar Contactos")
    if not agenda:
        print("⚠️ No hay contactos registrados")
    else:
        for nombre, datos in agenda.items():
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<25}")
        print("-" * 60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("🔎 Buscar Contacto")
    if not agenda:
        print("⚠️ No hay contactos registrados")
    else:
        nombre = input("Ingrese el nombre que desea buscar: ").upper().strip()
        if nombre in agenda:
            print(f"Nombre: {nombre}\n Teléfono: {agenda[nombre][0]}\n E-mail: {agenda[nombre][1]}")
            print("-" * 60)
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<10}")
            print("_"*60)
        else:
            print("❌ El contacto no se encuentra en la agenda")

def modificar_contacto(agenda):
    borrarPantalla()
    print("✏️ Modificar Contacto")
    if not agenda:
        print("No hay contactos en la agenda")
    else:
        nombre = input("Ingrese el nombre del contacto a modificar: ").upper().strip()
        # Verificar si el contacto existe
        if nombre in agenda:  # ¡Corrección clave!
            print("Valores actuales")
            print(f"Nombre: {nombre}\n Teléfono: {agenda[nombre][0]}\n E-mail: {agenda[nombre][1]}")
            resp = input("Deseas cambiar los valores? (Si/No)").upper().strip()
            if resp == "SI":
                tel = input("Telefono:").strip()
                email = input("Email: ").upper().strip()
                agenda[nombre] = [tel, email]
                print("Accion realizada con exito")
            else:
                print("Modificación cancelada")  # Mensaje corregido
        else:
            print("Este contacto no existe")  # Manejo de contacto inexistente

def eliminar_contacto(agenda):
    borrarPantalla()
    print("Eliminar Contacto")
    if not agenda:
        print("No hay contactos en la agenda")
    else:
        nombre = input("Ingrese el nombre del contacto a eliminar: ").upper().strip()  # Typo corregido
        # Verificar si el contacto existe
        if nombre in agenda:  # ¡Corrección clave!
            print("Valores actuales")
            print(f"Nombre: {nombre}\n Teléfono: {agenda[nombre][0]} \n E-mail: {agenda[nombre][1]}")
            resp = input("Deseas eliminar los valores? (Si/No)").upper().strip()
            if resp == "SI":
                agenda.pop(nombre)
                print("Accion realizada con exito")
            else:
                print("Eliminación cancelada")  # Mensaje corregido
        else:
            print("Este contacto no existe")  # Manejo de contacto inexistente