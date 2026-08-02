from funciones_inventario import agregar_producto, consultar_stock, modificar_stock

# --- 1. Añadimos productos reales de la ferretería ---
print("=== AÑADIENDO PRODUCTOS ===")
agregar_producto("Martillo", stock_inicial=15, precio=8.50)
agregar_producto("Tornillos 4mm", stock_inicial=500, precio=0.05)
agregar_producto("Caja de clavos", stock_inicial=40, precio=3.20)
agregar_producto("Destornillador plano", stock_inicial=25, precio=4.75)
agregar_producto("Cinta métrica", stock_inicial=10, precio=6.90)
agregar_producto("pulidora", stock_inicial=3, precio= 75.000)

# Probamos qué pasa si añadimos uno que ya existe (duplicado)
print("\n=== PROBANDO DUPLICADO ===")
agregar_producto("Martillo", stock_inicial=5, precio=9.00)

# --- 2. Consultamos stock de algunos productos ---
print("\n=== CONSULTANDO STOCK ===")
consultar_stock("Martillo")
consultar_stock("Tornillos 4mm")
consultar_stock("Producto que no existe")

# --- 3. Simulamos ventas (restamos stock) ---
print("\n=== SIMULANDO VENTAS ===")
modificar_stock("Martillo", -3)          # se venden 3 martillos
modificar_stock("Tornillos 4mm", -50)    # se venden 50 tornillos
modificar_stock("Caja de clavos", -100)  # intento de vender más de lo que hay

# --- 4. Simulamos una reposición (sumamos stock) ---
print("\n=== REPONIENDO STOCK ===")
modificar_stock("Cinta métrica", 20)     # llega mercancía nueva

# --- 5. Estado final ---
print("\n=== ESTADO FINAL DEL INVENTARIO ===")
consultar_stock("Martillo")
consultar_stock("Tornillos 4mm")
consultar_stock("Caja de clavos")
consultar_stock("Cinta métrica")