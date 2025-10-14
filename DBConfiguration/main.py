import psycopg2

def conectar():
    """Crea la conexión con la base de datos PostgreSQL."""
    return psycopg2.connect(
        host="localhost",             # 'db' es el nombre del servicio en docker-compose
        port="5432",
        database="credenciales",
        user="Admin",
        password="p4ssw0rdDB"
    )

def seleccionar(cursor):
    cursor.execute("SELECT * FROM usuarios;")
    registros = cursor.fetchall()
    if registros:
        for fila in registros:
            print(fila)
    else:
        print("No hay registros en la tabla usuarios.")

def insertar(cursor, conexion):
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    telefono = input("Teléfono: ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    
    cursor.execute("""
        INSERT INTO usuarios (nombre, correo, telefono, fecha_nacimiento)
        VALUES (%s, %s, %s, %s);
    """, (nombre, correo, telefono, fecha_nacimiento))
    conexion.commit()
    print("Usuario insertado correctamente.")

def actualizar(cursor, conexion):
    id_usuario = input("ID del usuario a actualizar: ")
    nuevo_nombre = input("Nuevo nombre: ")
    cursor.execute("""
        UPDATE usuarios
        SET nombre = %s
        WHERE id_usuario = %s;
    """, (nuevo_nombre, id_usuario))
    conexion.commit()
    print("Usuario actualizado correctamente.")

def eliminar(cursor, conexion):
    id_usuario = input("ID del usuario a eliminar: ")
    cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s;", (id_usuario,))
    conexion.commit()
    print("Usuario eliminado correctamente.")

def menu():
    conexion = conectar()
    cursor = conexion.cursor()

    while True:
        print("\n===== MENÚ DE OPCIONES =====")
        print("1. Seleccionar registros")
        print("2. Insertar nuevo usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            seleccionar(cursor)
        elif opcion == "2":
            insertar(cursor, conexion)
        elif opcion == "3":
            actualizar(cursor, conexion)
        elif opcion == "4":
            eliminar(cursor, conexion)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

    cursor.close()
    conexion.close()
    print("Conexión cerrada.")

if __name__ == "__main__":
    menu()