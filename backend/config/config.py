import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Variables de entorno con valores predeterminados
DB_USER = os.getenv("DB_USER", "system")
DB_PASS = os.getenv("DB_PASS", "12345")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "1521")
DB_SERVICE = os.getenv("DB_SERVICE", "XEPDB1")

# URI para SQLAlchemy (usando oracledb)
SQLALCHEMY_DATABASE_URI = f"oracle+oracledb://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/?service_name={DB_SERVICE}"
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Para evitar la advertencia de modificaciones no rastreadas

# Este bloque de código de conexión manual ya no es necesario cuando se usa SQLAlchemy
# try:
#     conn = oracledb.connect(
#         user=DB_USER,
#         password=DB_PASS,
#         dsn=f"{DB_HOST}:{DB_PORT}/{DB_SERVICE}"
#     )
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM SYSTEM.CUSTOMER")
#     rows = cursor.fetchall()
#     if rows:
#         for row in rows:
#             print(row)
#     cursor.close()
#     conn.close()
# except oracledb.DatabaseError as e:
#     print(f"Error al conectar con la base de datos: {e}")
#     exit(1)