import sqlite3

# Nombre de la base de datos que creamos antes
DB_NAME = "ferreteria_ruben_guerrero.db"

def agregar_producto(nombre, stock_inicial=0, precio=0.0):
    """Añade un producto nuevo a la ferretería"""
    try:
        conexion = sqlite3.connect(DB_NAME)
        cursor = conexion.cursor()
        
        # Insertamos el producto (pasamos el nombre en minúsculas para evitar duplicados por mayúsculas)
        cursor.execute("""
            INSERT INTO inventario (nombre, stock, precio) 
            VALUES (?, ?, ?)
        """, (nombre.lower(), stock_inicial, precio))
        
        conexion.commit()
        print(f"✅ Producto '{nombre}' agregado con éxito.")
    except sqlite3.IntegrityError:
        print(f"⚠️ El producto '{nombre}' ya existe en el inventario.")
    finally:
        conexion.close()
    

def consultar_stock(nombre):
    """Busca un producto y devuelve cuánto stock tiene"""
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    
    cursor.execute("SELECT stock, precio FROM inventario WHERE nombre = ?", (nombre.lower(),))
    resultado = cursor.fetchone()
    conexion.close()
    
    if resultado:
        stock, precio = resultado
        print(f"📦 Producto: {nombre.capitalize()} | Stock: {stock} unidades | Precio: ${precio}")
        return stock
    else:
        print(f"❌ El producto '{nombre}' no existe.")
        return None


def modificar_stock(nombre, cantidad):
    """Suma o resta unidades al stock de un producto"""
    conexion = sqlite3.connect(DB_NAME)
    cursor = conexion.cursor()
    
    # Primero verificamos si existe
    cursor.execute("SELECT stock FROM inventario WHERE nombre = ?", (nombre.lower(),))
    resultado = cursor.fetchone()
    
    if resultado:
        stock_actual = resultado[0]
        nuevo_stock = stock_actual + cantidad
        
        if nuevo_stock < 0:
            print(f"❌ No puedes vender {abs(cantidad)} unidades. Solo quedan {stock_actual} en stock.")
        else:
            cursor.execute("UPDATE inventario SET stock = ? WHERE nombre = ?", (nuevo_stock, nombre.lower()))
            conexion.commit()
            print(f"🔄 Stock actualizado. {nombre.capitalize()} ahora tiene {nuevo_stock} unidades.")
    else:
        print(f"❌ El producto '{nombre}' no existe para modificar su stock.")
        
    conexion.close()



