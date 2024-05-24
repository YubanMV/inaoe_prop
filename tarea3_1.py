def main():
    N = int(input("Ingrese el número de ventas realizadas: "))

    ventas_mayores_1000 = 0
    ventas_entre_500_y_1000 = 0
    ventas_menores_o_iguales_500 = 0

    monto_mayores_1000 = 0.0
    monto_entre_500_y_1000 = 0.0
    monto_menores_o_iguales_500 = 0.0

    for i in range(N):
        monto = float(input(f"Ingrese el monto de la venta {i+1}: "))
        if monto > 1000:
            ventas_mayores_1000 += 1
            monto_mayores_1000 += monto
        elif 500 < monto <= 1000:
            ventas_entre_500_y_1000 += 1
            monto_entre_500_y_1000 += monto
        else:
            ventas_menores_o_iguales_500 += 1
            monto_menores_o_iguales_500 += monto

    monto_total = monto_mayores_1000 + monto_entre_500_y_1000 + monto_menores_o_iguales_500

    print("\nResultados:")
    print(f"Ventas mayores a $1000: {ventas_mayores_1000}, Monto total: ${monto_mayores_1000:.2f}")
    print(f"Ventas mayores a $500 y menores o iguales a $1000: {ventas_entre_500_y_1000}, Monto total: ${monto_entre_500_y_1000:.2f}")
    print(f"Ventas menores o iguales a $500: {ventas_menores_o_iguales_500}, Monto total: ${monto_menores_o_iguales_500:.2f}")
    print(f"Monto total vendido: ${monto_total:.2f}")

if __name__ == "__main__":
    main()
