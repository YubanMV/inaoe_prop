def calcular_descuento_y_total(consumo, area):
    descuento = 0
    if area == "1":
        descuento = consumo * 0.35
    elif area == "2":
        descuento = consumo * 0.15
    elif area == "3" and consumo > 100:
        descuento = consumo * 0.10
    total_a_pagar = consumo - descuento
    return descuento, total_a_pagar

def main():
    while True:
        try:
            consumo = float(input("Introduce el monto total del consumo: $"))
            if consumo < 0:
                raise ValueError("El monto total del consumo no puede ser negativo.")
            
            area = input("Introduce el área del cliente (1, 2, 3): ")
            if area not in ["1", "2", "3"]:
                raise ValueError("Área no válida. Por favor, introduce un área válida (1, 2, 3).")
            
            descuento, total_a_pagar = calcular_descuento_y_total(consumo, area)

            print(f"Descuento aplicado: ${descuento:.2f}")
            print(f"Total a pagar: ${total_a_pagar:.2f}")
            
            break
        except ValueError as e:
            print(e)
            print("Inténtalo de nuevo.")


if __name__ == "__main__":
     main()