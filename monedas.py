def convertir_moneda(cantidad, moneda_origen, moneda_destino):
    tasas = {
        'USD': 1.0,
        'EUR': 0.85,
        'JPY': 110.0,
        'GBP': 0.75,
        'MXN': 20.0,
        'COP': 3800.0,
        'ARS': 95.0,
    }

    if moneda_origen not in tasas:
        return f"Error: La moneda {moneda_origen} no está disponible"
    
    if moneda_destino not in tasas:
        return f"Error: La moneda {moneda_destino} no está disponible"

    if moneda_origen == moneda_destino:
        return cantidad

    cantidad_en_dolares = cantidad / tasas[moneda_origen]
    resultado = cantidad_en_dolares * tasas[moneda_destino]

    return resultado

def main():
    print("CONVERSOR DE MONEDAS")
    print("=" * 20)
    
    monedas = ["USD", "EUR", "JPY", "GBP", "MXN", "COP", "ARS"]
    print("Monedas disponibles:", ", ".join(monedas))
    print()
    
    try:
        cantidad = float(input("¿Cuánto dinero quieres convertir? "))
        moneda_origen = input("¿De qué moneda? (ej: USD, EUR, COP): ").upper().strip()
        moneda_destino = input("¿A qué moneda? (ej: USD, EUR, COP): ").upper().strip()
        
        resultado = convertir_moneda(cantidad, moneda_origen, moneda_destino)
        
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"\n{cantidad} {moneda_origen} = {resultado:.2f} {moneda_destino}")
            
    except ValueError:
        print("Error: Por favor ingresa una cantidad numérica válida")
    except:
        print("Ocurrió un error inesperado")

if __name__ == "__main__":
    main()