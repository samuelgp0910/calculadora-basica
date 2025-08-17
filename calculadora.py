def calculadora():
    print("calculadoratomas")
    print("si quieres 'salir'solo escribelo")

    while True: 
        operacion = input("Introduce la operación (suma, resta, multiplicacion o división): ").strip()
        if operacion.lower() == 'salir':
            print("Saliendo de la calculadora.")
            break
        if operacion not in ['suma', 'resta', 'multiplicacion', 'division']:
            print("Operación no válida. Por favor, elige entre suma, resta, multiplicación o división.")
            continue
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("como asi?. Por favor, introduce números válidos.")
            continue
        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            if num2 == 0:
                print("No se puede dividir por cero.")
                continue
            resultado = num1 / num2
        
        print(f"El resultado de la {operacion} es: {resultado}")
        print("¿Quieres hacer otra operación? (si/no)")
        otra_operacion = input().strip().lower()
        if otra_operacion != 'si':
            print("Saliendo de la calculadora.")
            break
calculadora()    