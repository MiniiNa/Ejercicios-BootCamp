import random

numero_secreto = random.randint(1, 100)
print(numero_secreto)
intentos = 0

print("He pensado un número entre 1 y 100")

while True:
    intento = int(input("Tu intento: "))
    intentos += 1

    if intento < numero_secreto:
        print("Más alto")
    elif intento > numero_secreto:
        print("Más bajo")
    else:
        print(f"¡CORRECTO! En {intentos} intentos")
        break