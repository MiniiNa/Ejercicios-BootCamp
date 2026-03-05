while True:
    numero_usuario = int(input("Introduce un número entre 1 y 100: "))

    if numero_usuario >100 or numero_usuario < 1:
        print("Número fuera de rango. Intenta de nuevo.")
        continue
    else:
        if numero_usuario %2 == 0:
            print(f"{numero_usuario} es un número par.")

        else:
            print(f"{numero_usuario} es un número impar.")
        break