def verificador_de_contraseñas():
    print("Bienvenido al verificador de contraseñas.")
while True:
    contrasena = input("Introduce la contraseña a verificar (o escribe 'salir' para terminar): ").strip()
    if contrasena.lower() == 'salir':
        print("Saliendo del verificador de contraseñas.")
        break

    if len(contrasena) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        continue
    if not any(char.isdigit() for char in contrasena):
        print("La contraseña debe contener al menos un número.")
        continue
    if not any(char.isalpha() for char in contrasena):
        print("La contraseña debe contener al menos una letra.")
        continue
    if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in contrasena):
        print("La contraseña debe contener al menos un carácter especial.")
        continue
    print("La contraseña es válida.")
    otra_verificacion = input("¿Quieres verificar otra contraseña? (si/no): ").strip().lower()
    if otra_verificacion != 'si':
        print("Saliendo del verificador de contraseñas.")
        break
verificador_de_contraseñas()
