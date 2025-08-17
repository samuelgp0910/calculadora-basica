def juego():
    import random
    numero = random.randint(1, 10)
    print("Bienvenido al juego de adivinar el número.")
    intentos = 5

    for i in range(intentos):
        try:
            adivina = int(input("Adivina el número (entre 1 y 10): "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if adivina < 1 or adivina > 10:
            print("El número debe estar entre 1 y 10.")
            continue

        if adivina == numero:
            print("¡Felicidades! Has adivinado el número.")
            break
        else:
            if adivina < numero:
                print("El número es mayor.")
            else:
                print("El número es menor.")
    else:
        print(f"Lo siento, no has adivinado el número. Era {numero}.")
    print("Fin del juego.")
    otra_jugada = input("¿Quieres jugar de nuevo? (si/no): ").strip().lower()
    if otra_jugada == 'si':
        juego()
    else:
        print("Gracias por jugar. ¡Hasta luego!")
juego()