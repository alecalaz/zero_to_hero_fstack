#mutables ejemplo con diccionarios
user = {"name": "Maria", "age": 28, "city": "Buenos Aires"}
print("Original:", user)

# Modificar un valor existente
user["age"] = 29
print("Despues de modificar:", user)

# Eliminar un par clave-valor
del user["city"]
print("Despues de eliminar:", user)

#mutables ejemplo con listas
tasks = ["buy groceries", "send email", "call doctor"]
print("Original:", tasks)

# Reemplazar un elemento
tasks[1] = "send report"
print("Despues de reemplazar:", tasks)

# Agregar un nuevo elemento
tasks.append("read book")
print("Despues de agregar:", tasks)

# Eliminar un elemento
tasks.remove("call doctor")
print("Despues de eliminar:", tasks)