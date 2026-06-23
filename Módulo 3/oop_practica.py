# ============================================================
#  OOP — Programación Orientada a Objetos
#  Módulo 3 → Intermedio | Ejercicios anotados para Ale
# ============================================================

# ────────────────────────────────────────────────────────────
# PARTE 1: Anatomía de una clase completa
# ────────────────────────────────────────────────────────────

class BankAccount:
    """
    Clase que representa una cuenta bancaria.
    Analogía: esta clase ES el molde. Cada cuenta que crees
    es un objeto (instancia) distinto con su propio saldo y dueño.
    """

    # ── Constructor (__init__) ────────────────────────────────
    # Se ejecuta AUTOMÁTICAMENTE cada vez que haces BankAccount(...)
    # Sus parámetros (owner, initial_balance) son variables locales.
    # Para que persistan como datos del objeto, debes guardarlos con self.
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner                  # atributo de instancia
        self.balance = initial_balance      # atributo de instancia
        self.transactions = []              # lista propia de ESTE objeto
        print(f"Cuenta creada para {self.owner} con ${self.balance:.2f}")

    # ── Métodos ───────────────────────────────────────────────
    # self = el objeto que llamó al método.
    # Python convierte: account.deposit(500) → BankAccount.deposit(account, 500)

    def deposit(self, amount: float):
        if amount <= 0:
            print("El monto debe ser positivo.")
            return
        self.balance += amount
        self.transactions.append(f"+${amount:.2f}")
        print(f"Depósito de ${amount:.2f}. Saldo actual: ${self.balance:.2f}")

    def withdraw(self, amount: float):
        if amount <= 0:
            print("El monto debe ser positivo.")
            return
        if amount > self.balance:
            print(f"Fondos insuficientes. Saldo: ${self.balance:.2f}")
            return
        self.balance -= amount
        self.transactions.append(f"-${amount:.2f}")
        print(f"Retiro de ${amount:.2f}. Saldo actual: ${self.balance:.2f}")

    def show_statement(self):
        print(f"\n── Estado de cuenta: {self.owner} ──")
        if not self.transactions:
            print("Sin movimientos.")
        for t in self.transactions:
            print(f"  {t}")
        print(f"  Saldo final: ${self.balance:.2f}\n")


# ─── Prueba: dos cuentas, totalmente independientes ──────────
print("=" * 45)
ale_account = BankAccount("Alejandro", 1000.0)
maria_account = BankAccount("María", 500.0)

ale_account.deposit(200)
ale_account.withdraw(50)
maria_account.deposit(1000)

ale_account.show_statement()
maria_account.show_statement()

# Observa: ale_account.transactions ≠ maria_account.transactions
# Son listas distintas. Cada objeto tiene la suya.


# ────────────────────────────────────────────────────────────
# PARTE 2: self en detalle — entendiendo lo que Python hace
# ────────────────────────────────────────────────────────────

class Counter:
    def __init__(self, name: str):
        self.name = name
        self.count = 0

    def increment(self):
        self.count += 1   # self.count = self.count + 1

    def reset(self):
        self.count = 0

    def value(self):
        return self.count


counter_a = Counter("A")
counter_b = Counter("B")

counter_a.increment()
counter_a.increment()
counter_a.increment()
counter_b.increment()

print(counter_a.name, counter_a.value())  # A 3
print(counter_b.name, counter_b.value())  # B 1

# Python convierte counter_a.increment() en → Counter.increment(counter_a)
# Por eso self dentro de increment() hace referencia a counter_a,
# y self.count es el count de counter_a, no de counter_b.


# ────────────────────────────────────────────────────────────
# PARTE 3: El bug del atributo de clase (¡importante!)
# ────────────────────────────────────────────────────────────

# ❌ MAL — photographies es un atributo de CLASE, compartido por todos
class CameraBuggy:
    photos = []   # ← todas las instancias comparten esta misma lista

    def take_photo(self, photo):
        self.photos.append(photo)


cam1 = CameraBuggy()
cam2 = CameraBuggy()
cam1.take_photo("Foto de mi casa")
print(cam2.photos)  # ['Foto de mi casa'] ← bug: cam2 ve las fotos de cam1


# ✅ BIEN — photos como atributo de instancia dentro del __init__
class CameraFixed:
    def __init__(self):
        self.photos = []   # ← lista nueva, propia de cada objeto

    def take_photo(self, photo):
        self.photos.append(photo)


cam3 = CameraFixed()
cam4 = CameraFixed()
cam3.take_photo("Foto de mi casa")
print(cam4.photos)  # [] ← correcto: cam4 no tiene fotos propias


# ────────────────────────────────────────────────────────────
# PARTE 4: name vs self.name — diferencia crítica
# ────────────────────────────────────────────────────────────

class Person:
    def __init__(self, name: str, age: int):
        # name  → variable local del constructor (desaparece al salir de __init__)
        # age   → variable local del constructor (desaparece al salir de __init__)

        self.name = name   # ← ahora name vive como atributo del objeto
        self.age = age     # ← ahora age vive como atributo del objeto

        local_var = "solo existo aquí"   # solo vive dentro de __init__

    def greet(self):
        # self.name → accede al atributo del objeto (persiste)
        print(f"Hola, soy {self.name} y tengo {self.age} años")
        # print(local_var)  # ← AttributeError: no existe fuera del __init__


p = Person("Alejandro", 28)
p.greet()
print(p.name)   # ← "Alejandro"
# print(name)   # ← NameError: name no existe aquí, era local del __init__


# ────────────────────────────────────────────────────────────
# PARTE 5: Ejemplo conectado a tu trabajo (IT / Cloud)
# ────────────────────────────────────────────────────────────

class AzureVM:
    """Representa una Virtual Machine en Azure."""

    def __init__(self, vm_name: str, size: str, region: str):
        self.vm_name = vm_name
        self.size = size
        self.region = region
        self.status = "stopped"      # las VMs nacen apagadas
        self.tags = {}

    def start(self):
        if self.status == "running":
            print(f"{self.vm_name} ya está corriendo.")
            return
        self.status = "running"
        print(f"✅ {self.vm_name} iniciada en {self.region}")

    def stop(self):
        if self.status == "stopped":
            print(f"{self.vm_name} ya está apagada.")
            return
        self.status = "stopped"
        print(f"🛑 {self.vm_name} detenida.")

    def add_tag(self, key: str, value: str):
        self.tags[key] = value
        print(f"Tag agregado: {key} = {value}")

    def info(self):
        print(f"\n── {self.vm_name} ──")
        print(f"  Size:   {self.size}")
        print(f"  Region: {self.region}")
        print(f"  Status: {self.status}")
        print(f"  Tags:   {self.tags}")


# Simula tu trabajo diario en Azure
web_server = AzureVM("web-prod-01", "Standard_D2s_v3", "eastus")
db_server  = AzureVM("db-prod-01",  "Standard_E4s_v3", "eastus")

web_server.start()
web_server.add_tag("env", "production")
web_server.add_tag("owner", "ale")

db_server.start()
db_server.add_tag("env", "production")

web_server.info()
db_server.info()

# Las VMs son independientes — exactamente como los objetos.
# Apagar una no afecta a la otra.
web_server.stop()
print(f"\nweb_server: {web_server.status}")
print(f"db_server:  {db_server.status}")   # sigue running


# ────────────────────────────────────────────────────────────
# EJERCICIOS — Completa los TODOs
# ────────────────────────────────────────────────────────────

# EJERCICIO 1:
# Crea una clase `Student` con:
# - Atributos: name, age, grades (lista vacía por defecto)
# - Método add_grade(grade): agrega una nota a la lista
# - Método average(): retorna el promedio de las notas
# - Método passed(): retorna True si el promedio >= 60
#
# TODO: escribe tu clase aquí
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []


    def add_grade(self,grade):
        self.grades.append(grade)
    

    def average(self):
        self.avrg = sum(self.grades) / len(self.grades)
        return self.avrg
        


    def passed(self):
        if self.avrg >= 60 :
            return True
        else:
            return False


# EJERCICIO 2:
# Crea una clase `ServerMonitor` que:
# - En __init__ reciba server_name y max_cpu_threshold (%)
# - Tenga un método check_cpu(current_cpu) que:
#   → Si current_cpu >= max_cpu_threshold: imprime una alerta
#   → Si no: imprime que todo está bien
# - Tenga un método log que guarde cada lectura en una lista interna
#
# Tip: usa tu experiencia de Azure Active Directory como inspiración
#
# TODO: escribe tu clase aquí

class ServerMonitor:
    def __init__(self, server_name, max_cpu_threshold):
        self.server_name = server_name
        self.max_cpu_threshold = max_cpu_threshold
        self.logs = []
    

    def check_cpu(self, current_cpu):
        if current_cpu >= self.max_cpu_threshold:
            print(f'Alerta {current_cpu} es igual o mayor a {self.max_cpu_threshold}. {self.server_name}')
            self.logs.append(f'Alerta critica, {current_cpu} es igual o mayor a {self.max_cpu_threshold}. {self.server_name}')
        else:
            print('Todo esta bien')
            self.logs.append(f'{self.server_name} tiene actualmente {current_cpu}')
        
    





# EJERCICIO 3 (desafío):
# Crea una clase `ADUser` (Active Directory User) con:
# - Atributos: username, email, department, is_active (True por default)
# - Método disable(): cambia is_active a False
# - Método enable(): cambia is_active a True
# - Método reset_password(new_password): solo funciona si is_active es True
# - Método info(): imprime todos los datos del usuario
#
# TODO: escribe tu clase aquí

class AdUser:
    def __init__(self, username, email, department, is_active = True):
        self.username = username
        self.email = email
        self.department = department
        self.active = is_active
        self.password = ''

    def disable(self):
        self.active = False
    
    def enable(self):
        if self.active == True:
            print('Ya esta activo!')
        else:
            self.active = True
    
    def reset_password(self, new_password):
        if self.active == True:
            self.password = new_password
        else:
            print('el usuario debe estar activo primero!')
    
    def info(self):
        print(vars(self))