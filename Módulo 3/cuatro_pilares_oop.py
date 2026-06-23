# ============================================================
#  LOS 4 PILARES DE OOP — Ejemplos con contexto IT/Cloud
#  Módulo Intermedio | Para Alejandro
# ============================================================

# ────────────────────────────────────────────────────────────
# PILAR 1: HERENCIA
# "No repitas lo que ya existe. Extiéndelo."
# ────────────────────────────────────────────────────────────
#
# Escenario: sistema de recursos cloud (VMs, Containers, Functions)
# Todos son "recursos", pero cada uno tiene características propias.

class CloudResource:
    """Clase padre — todo recurso cloud tiene esto en común."""
    def __init__(self, name: str, region: str):
        self.name = name
        self.region = region
        self.status = "stopped"

    def start(self):
        self.status = "running"
        print(f"[{self.name}] iniciado en {self.region}")

    def stop(self):
        self.status = "stopped"
        print(f"[{self.name}] detenido")

    def info(self):
        print(f"{self.name} | region: {self.region} | status: {self.status}")


class VirtualMachine(CloudResource):
    """Hereda todo de CloudResource y agrega lo propio de una VM."""
    def __init__(self, name, region, size):
        super().__init__(name, region)   # ← llama el __init__ del padre
        self.size = size
        self.os = "Windows Server"

    def info(self):
        super().info()                   # ← reutiliza el info() del padre
        print(f"  size: {self.size} | OS: {self.os}")


class Container(CloudResource):
    """También hereda de CloudResource, pero con sus propias cosas."""
    def __init__(self, name, region, image):
        super().__init__(name, region)
        self.image = image

    def info(self):
        super().info()
        print(f"  image: {self.image}")


# ─── Prueba ────────────────────────────────────────────────
vm = VirtualMachine("web-prod-01", "eastus", "Standard_D2s")
container = Container("api-container", "westus", "nginx:latest")

vm.start()
vm.info()
container.start()
container.info()

# 🤔 PREGUNTA: ¿Por qué usamos super().__init__() en lugar de
#    repetir self.name = name, self.region = region, etc.?
#    ¿Qué pasaría si mañana agregas un atributo nuevo a CloudResource?


# ────────────────────────────────────────────────────────────
# PILAR 2: ENCAPSULAMIENTO
# "Protege el estado interno. Controla cómo se modifica."
# ────────────────────────────────────────────────────────────
#
# El punto NO es que sea imposible acceder.
# El punto es que OBLIGAS a pasar por métodos que validan.
#
# Escenario: cuenta de servicio en Azure con límite de permisos.

class ServiceAccount:
    def __init__(self, name: str, role: str):
        self.name = name
        self._role = role           # _ = "no toques esto directamente"
        self.__secret_key = None    # __ = "esto es interno, punto"
        self._permissions = []

    # Método público que expone el rol de forma controlada
    def get_role(self):
        return self._role

    # Para cambiar el rol, pasas por aquí (puedes agregar validaciones)
    def set_role(self, new_role: str):
        valid_roles = ["reader", "contributor", "owner"]
        if new_role not in valid_roles:
            print(f"Rol inválido: {new_role}. Opciones: {valid_roles}")
            return
        self._role = new_role
        print(f"[{self.name}] rol actualizado a: {new_role}")

    def assign_permission(self, permission: str):
        self._permissions.append(permission)

    def rotate_secret(self, new_key: str):
        """Solo este método puede cambiar el secret key."""
        self.__secret_key = new_key
        print(f"[{self.name}] secret key rotado correctamente")

    def info(self):
        print(f"\n── ServiceAccount: {self.name} ──")
        print(f"  Role:        {self._role}")
        print(f"  Permissions: {self._permissions}")
        print(f"  Has secret:  {self.__secret_key is not None}")


# ─── Prueba ────────────────────────────────────────────────
svc = ServiceAccount("svc-deploy", "contributor")
svc.info()

# Intentar asignar un rol inválido → bloqueado por el método
svc.set_role("god_mode")    # ← imprime error
svc.set_role("reader")      # ← funciona

# Rotar el secreto
svc.rotate_secret("abc123xyz")
svc.info()

# Sin encapsulamiento, cualquiera podría hacer esto y romper todo:
# svc._role = "god_mode"         ← técnicamente funciona en Python,
# svc.__secret_key = "hackeado"  ← pero __secret_key está name-mangled
#                                    → en realidad es _ServiceAccount__secret_key

# 🤔 PREGUNTA: ¿Por qué es importante que rotate_secret sea el ÚNICO
#    método que cambia __secret_key? ¿Qué validaciones podrías
#    agregar ahí en el mundo real (longitud mínima, caracteres, etc.)?


# ────────────────────────────────────────────────────────────
# PILAR 3: ABSTRACCIÓN
# "El que usa tu clase no necesita saber cómo funciona por dentro."
# ────────────────────────────────────────────────────────────
#
# Abstracción ≠ Encapsulamiento. La diferencia:
#   Encapsulamiento → esconde el estado interno (los DATOS)
#   Abstracción     → simplifica la interfaz pública (las ACCIONES)
#
# Juntos: el usuario ve métodos simples y claros,
#         sin saber (ni importarle) qué pasa adentro.
#
# Escenario: sistema de provisioning de usuarios en Azure AD.
# El que llama a este objeto solo hace: provision() o deprovision()
# No sabe nada de los pasos internos.

from abc import ABC, abstractmethod

class IdentityProvider(ABC):
    """Clase abstracta — define el contrato que todo proveedor debe cumplir."""

    @abstractmethod
    def _create_user(self, username: str):
        """Cada proveedor crea usuarios a su manera."""
        pass

    @abstractmethod
    def _assign_license(self, username: str):
        pass

    @abstractmethod
    def _send_welcome_email(self, username: str):
        pass

    # Este método público es la ABSTRACCIÓN:
    # El usuario llama provision() y listo. No sabe los 3 pasos de adentro.
    def provision(self, username: str):
        print(f"\nProvisionando {username}...")
        self._create_user(username)
        self._assign_license(username)
        self._send_welcome_email(username)
        print(f"✅ {username} listo.")


class AzureADProvider(IdentityProvider):
    """Implementación concreta para Azure AD."""

    def _create_user(self, username: str):
        print(f"  → Creando usuario en Azure AD: {username}")

    def _assign_license(self, username: str):
        print(f"  → Asignando licencia M365 E3 a {username}")

    def _send_welcome_email(self, username: str):
        print(f"  → Enviando email de bienvenida a {username}@empresa.com")


class OktaProvider(IdentityProvider):
    """Implementación concreta para Okta."""

    def _create_user(self, username: str):
        print(f"  → Creando usuario en Okta: {username}")

    def _assign_license(self, username: str):
        print(f"  → Asignando grupo Okta 'employees' a {username}")

    def _send_welcome_email(self, username: str):
        print(f"  → Disparando workflow de onboarding en Okta para {username}")


# ─── Prueba ────────────────────────────────────────────────
azure_provider = AzureADProvider()
okta_provider = OktaProvider()

# El que llama esto no sabe NI le importa lo que pasa adentro
azure_provider.provision("ale.castano")
okta_provider.provision("maria.lopez")

# Intentar instanciar la clase abstracta → error
# provider = IdentityProvider()   # ← TypeError

# 🤔 PREGUNTA: El método provision() está en la clase padre y llama
#    a _create_user, _assign_license, _send_welcome_email.
#    ¿Por qué esos tres métodos empiezan con _ ?
#    ¿Qué indica eso sobre quién debería llamarlos?


# ────────────────────────────────────────────────────────────
# PILAR 4: POLIMORFISMO
# "Mismo mensaje, comportamiento distinto según quien lo recibe."
# ────────────────────────────────────────────────────────────
#
# No necesitas saber qué tipo de objeto tienes.
# Solo necesitas saber que tiene el método que buscas.
#
# Escenario: sistema de notificaciones. Puede enviar por email,
# Teams, o Slack. El código que los llama no cambia.

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class EmailNotifier(Notifier):
    def __init__(self, recipient: str):
        self.recipient = recipient

    def send(self, message: str):
        print(f"[EMAIL → {self.recipient}] {message}")


class TeamsNotifier(Notifier):
    def __init__(self, channel: str):
        self.channel = channel

    def send(self, message: str):
        print(f"[TEAMS → #{self.channel}] {message}")


class SlackNotifier(Notifier):
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send(self, message: str):
        print(f"[SLACK → {self.webhook_url[:30]}...] {message}")


# ─── Prueba: polimorfismo en acción ────────────────────────
# Esta función no sabe qué tipo de notifier recibe.
# Solo sabe que tiene .send(). Eso es polimorfismo.
def alert_team(notifiers: list, message: str):
    for notifier in notifiers:
        notifier.send(message)


notifiers = [
    EmailNotifier("ale@empresa.com"),
    TeamsNotifier("alertas-prod"),
    SlackNotifier("https://hooks.slack.com/services/xxx/yyy/zzz"),
]

alert_team(notifiers, "⚠️ CPU > 90% en web-prod-01")

# 🤔 PREGUNTA: Si mañana agregas un WhatsAppNotifier,
#    ¿tienes que cambiar la función alert_team()?
#    ¿Por qué sí o por qué no?


# ────────────────────────────────────────────────────────────
# RESUMEN VISUAL: diferencia entre los 4 pilares
# ────────────────────────────────────────────────────────────
#
#  HERENCIA       → "Soy como tú, pero con extras"
#                   VirtualMachine hereda de CloudResource
#
#  ENCAPSULAMIENTO → "Mis datos internos se protegen"
#                   __secret_key solo se cambia con rotate_secret()
#
#  ABSTRACCIÓN    → "Tú llamas provision(), yo me encargo del resto"
#                   Los pasos _create_user, _assign_license, etc. son invisibles
#
#  POLIMORFISMO   → "Mismo método, distinto comportamiento"
#                   email.send(), teams.send(), slack.send() → misma firma, distinta acción
#
# ────────────────────────────────────────────────────────────
# EJERCICIO: Diseña tu propio sistema
#
# Crea un sistema de backup para servidores con:
# - Una clase abstracta `BackupStrategy` con método abstracto `backup(server_name)`
# - Clase `LocalBackup` que imprime "Copiando [server] a disco local"
# - Clase `AzureBlobBackup` que imprime "Subiendo [server] a Azure Blob Storage"
# - Clase `S3Backup` que imprime "Subiendo [server] a AWS S3"
# - Una función `run_backups(strategies, server_name)` que ejecuta todas las estrategias
#
# Tip: es casi idéntico al ejemplo de Notifier. Inténtalo sin mirar ese ejemplo.
# ────────────────────────────────────────────────────────────
