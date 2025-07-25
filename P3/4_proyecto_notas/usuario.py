import datetime
import hashlib
import conexionBD

def password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

import traceback
import datetime
import hashlib
import conexionBD

def password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre, apellidos, email, contrasena):
    try:
        conexion = conexionBD.obtener_conexion()
        if conexion is None:
            print("Error: no se pudo conectar a la base de datos")
            return False
        cursor = conexion.cursor()
        fecha = datetime.datetime.now()
        contrasena_hash = password(contrasena)
        cursor.execute(
            "INSERT INTO usuarios (nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, %s)",
            (nombre, apellidos, email, contrasena_hash, fecha)
        )
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print("Error al registrar:")
        traceback.print_exc()
        return False


def inicio_sesion(email, contrasena):
    try:
        conexion = conexionBD.obtener_conexion()
        if conexion is None:
            print("No se pudo conectar a la base de datos")
            return None
        cursor = conexion.cursor()

        email = email.lower().strip()
        contrasena = contrasena.strip()
        contrasena_hash = password(contrasena)

        print(f"Email recibido para login: '{email}'")
        print(f"Hash de la contraseña recibida: '{contrasena_hash}'")

        cursor.execute(
            "SELECT * FROM usuarios WHERE email = %s AND password = %s",
            (email, contrasena_hash)
        )
        usuario = cursor.fetchone()
        cursor.close()
        conexion.close()
        return usuario
    except Exception as e:
        print("Error al iniciar sesión:", e)
        return None

