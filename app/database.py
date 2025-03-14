import oracledb  # Importar la librería para conectar con Oracle

# Datos de conexión
usuario = "system"
contraseña = "12345"
dsn = "localhost:1521/XEPDB1"  # Cambia "XEPDB1" a "XE" si es necesario

try:
    # Conectar a la base de datos
    conexion = oracledb.connect(user=usuario, password=contraseña, dsn=dsn)
    cursor = conexion.cursor()  # Crear un cursor para ejecutar consultas

    # Ejecutar la consulta SQL
    cursor.execute("SELECT * FROM SYSTEM.CUSTOMER")
    filas = cursor.fetchall()  # Obtener todos los registros

    # Mostrar los resultados
    if filas:
        for fila in filas:
            print(fila)
    else:
        print("No hay registros en la tabla CUSTOMER.")

except oracledb.DatabaseError as error:
    print("Error al conectar con la base de datos:", error)

finally:
    # Cerrar cursor
    if 'cursor' in locals():
        cursor.close()
    if 'conexion' in locals():
        conexion.close()