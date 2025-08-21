import random
def obtener_palabra_secreta():
    palabras = ['tomas', 'paola', 'fabian', 'samuel']
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ''
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + ' '
        else:
            tablero += '_ '
            print(tablero)

def jugar_ahorcado():
    palabra_secreta= obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 6

    while intentos > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra=input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue
        
        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            if set(letras_adivinadas) >= set(palabra_secreta):
                print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
                break
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")
    if intentos == 0:
        print(f"Has perdido. La palabra era: {palabra_secreta}")
jugar_ahorcado()

