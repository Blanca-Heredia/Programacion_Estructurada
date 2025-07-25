calificaciones=[]

def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("🔸 Oprima cualquier tecla para continuar...")

def menu_principal():
    print("📚  GESTIÓN DE CALIFICACIONES 📚")
    print("1️⃣  Agregar")
    print("2️⃣  Mostrar")
    print("3️⃣  Calcular promedios")
    print("4️⃣  Salir")
    opcion = input("➡️  Elige una opción: ").upper()
    return opcion

def agregarCalificaciones(lista):
    borrarPantalla()
    print("📝 Agregar calificaciones")
    nombre = input("👤 Nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        continua = True
        while continua:
            try:
                cal = float(input(f"✏️ Ingresa la calificación #{i}: "))
                if cal >= 0 and cal <= 10:
                    calificaciones.append(cal)
                    continua = False
                else:
                    print("⚠️ La calificación debe estar entre 0 y 10")
            except ValueError:
                print("❌ Ingresa un valor numérico")
    lista.append([nombre] + calificaciones)
    print("✅ ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO!")

def mostrarCalificaciones(lista):
    borrarPantalla()
    print("📋 Mostrar TODAS las calificaciones")
    if len(lista) > 0:
        print(f"{'Nombre':<15}  {'Calificación 1':<15}  {'Calificación 2':<15}  {'Calificación 3':<15}")
        print("-" * 60)
        for fila in lista:
            print(f"{fila[0]:<15}  {fila[1]:<15}  {fila[2]:<15}  {fila[3]:<15}")
        print("-" * 60)
        cuantos = len(lista)
        print(f"👥 Son {cuantos} alumnos")
    else:
        print("⚠️ No hay calificaciones en el sistema")

def calcularCalificaciones(lista):
    borrarPantalla()
    print("📊 Promedios de los alumnos")
    if len(lista) > 0:
        print(f"{'Nombre':<15}  {'Promedio':<15} ")
        print("-" * 40)
        promedio_grupal = 0
        for fila in lista:
            nombre = fila[0]
            promedio = sum(fila[1:]) / 3
            print(f"{nombre:<15}  {promedio:.2f}")
            promedio_grupal += promedio
            print("-" * 40)
        promedio_grupal = promedio_grupal / len(lista)
        print(f"📈 El promedio del grupo es: {promedio_grupal:.2f}")
    else:
        print("⚠️ No hay calificaciones en el sistema")
