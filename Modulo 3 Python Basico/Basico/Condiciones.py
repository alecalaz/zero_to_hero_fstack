has_ticket = True
age = 20
min_age = 18

if has_ticket:
    print("Tienes boleto, verifiquemos tu edad... 🎟️")

    # Este if vive dentro del anterior
    # Solo se ejecuta si has_ticket es True
    if age >= min_age:
        print("¡Bienvenido a la función! 🍿")
    else:
        print("Lo sentimos, eres menor de edad para esta película 🔞")

else:
    print("Por favor compra un boleto en taquilla 🎫")


# Solicitamos la opción al usuario
option = int(input("Selecciona una opción (1-3): "))

# Siempre validamos el valor de la variable option
match option:
    case 1:
        print("Ver perfil 👤")
    case 2:
        print("Ir a Configuración ⚙️")
    case 3:
        print("Cerrar sesión 👋")
    case _:
        print("Opción no válida 🚫")
