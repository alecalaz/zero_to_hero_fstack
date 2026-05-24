import csv

# ── Configura los nombres de los archivos CSV aquí ──────────────────────────
ARCHIVO_DEVICES_OBJETIVO = "devices_objetivo.csv"   # CSV 1: solo tiene deviceId
ARCHIVO_TODOS_LOS_DEVICES = "todos_los_devices.csv" # CSV 2: tiene deviceId + id (object id)
ARCHIVO_SALIDA = "object_ids_para_entra.csv"        # resultado para el bulk update
# ─────────────────────────────────────────────────────────────────────────────

# Paso 1: leer los device IDs que quiero actualizar (CSV 1)
device_ids_objetivo = []
with open(ARCHIVO_DEVICES_OBJETIVO, newline="", encoding="utf-8-sig") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        device_ids_objetivo.append(fila["deviceId"].strip())

print(f"Devices a actualizar encontrados: {len(device_ids_objetivo)}")

# Paso 2: leer todos los devices con sus object IDs (CSV 2) y armar un diccionario
# clave = deviceId, valor = id (object id de Entra)
mapa_device_a_object_id = {}
with open(ARCHIVO_TODOS_LOS_DEVICES, newline="", encoding="utf-8-sig") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        mapa_device_a_object_id[fila["deviceId"].strip()] = fila["id"].strip()

print(f"Total de devices en el archivo de referencia: {len(mapa_device_a_object_id)}")

# Paso 3: buscar el object ID de cada device objetivo
object_ids_encontrados = []
no_encontrados = []

for device_id in device_ids_objetivo:
    if device_id in mapa_device_a_object_id:
        object_ids_encontrados.append(mapa_device_a_object_id[device_id])
    else:
        no_encontrados.append(device_id)

# Paso 4: escribir el CSV de salida con los object IDs
with open(ARCHIVO_SALIDA, "w", newline="", encoding="utf-8-sig") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["id"])  # encabezado que usa el template de Entra
    for object_id in object_ids_encontrados:
        escritor.writerow([object_id])

# Paso 5: mostrar resumen
print(f"\nObject IDs encontrados y guardados: {len(object_ids_encontrados)}")
print(f"Archivo de salida creado: {ARCHIVO_SALIDA}")

if no_encontrados:
    print(f"\nATENCION - {len(no_encontrados)} device(s) no se encontraron en el CSV de referencia:")
    for d in no_encontrados:
        print(f"  - {d}")
