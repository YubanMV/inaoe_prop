def calcular_ahorro_final(ahorro_inicial, años=5):
    meses_totales = años * 12
    ahorro_total = ahorro_inicial  # Inicialmente se ingresa la cantidad inicial

    print(f"Mes 0: Ahorro total = ${ahorro_total:.2f}")

    for mes in range(1, meses_totales + 1):
        # Incrementar el ahorro mensual basado en el monto total actual
        if ahorro_total > 2 * ahorro_inicial:
            incremento = 0.05 * ahorro_total
            tipo_incremento = "5%"
        else:
            incremento = 0.03 * ahorro_total
            tipo_incremento = "3%"

        ahorro_total += incremento

        # Cada año, agregar un 10% del monto inicial de ahorro
        if mes % 12 == 0:
            incremento_anual = 0.10 * ahorro_inicial
            ahorro_total += incremento_anual
            #print(f"Mes {mes}: Se añade un incremento anual de ${incremento_anual:.2f} del ahorro inicial")

        #print(f"Mes {mes}: Incremento mensual = ${incremento:.2f} ({tipo_incremento}), Ahorro total = ${ahorro_total:.2f}")

    return ahorro_total

def main():
    ahorro_inicial = float(input("Ingrese la cantidad inicial de ahorro mensual: "))
    ahorro_final = calcular_ahorro_final(ahorro_inicial)
    print(f"El monto total ahorrado al final de 5 años es: ${ahorro_final:.2f}")

if __name__ == "__main__":
    main()
