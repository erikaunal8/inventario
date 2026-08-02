import sqlite3

def inicializar_base_datos():
    # Cambiamos el nombre del archivo aquí
    conexion = sqlite3.connect("ferreteria_ruben_guerrero.db")
    
    cursor = conexion.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            stock INTEGER DEFAULT 0,
            precio REAL DEFAULT 0.0,
            ruta_imagen TEXT
        )
    """)
    
    conexion.commit()
    conexion.close()
    print("¡Base de datos de la Ferretería Rubén Guerrero creada con éxito!")

if __name__ == "__main__":
    inicializar_base_datos()