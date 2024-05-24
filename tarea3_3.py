while True:
    try:
        # Solicitar al usuario que ingrese un número del 1 al 20
        n = int(input("Ingresa un número del 1 al 20: "))

        # Verificar si el número está dentro del rango válido
        if 1 <= n <= 20:
            break
        else:
            print("Error: El número debe estar entre 1 y 20.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

# Generar e imprimir el triángulo de números
for i in range(1, n + 1):
    print(str(i) * i)
