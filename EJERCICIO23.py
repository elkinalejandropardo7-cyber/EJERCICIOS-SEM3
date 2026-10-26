
import random

secreto = random.randint(1, 10)
numero = 0

while numero != secreto:
    numero = int(input("Adivina el número secreto (1 al 10): "))

    if numero < secreto:
        print("El número secreto es mayor.")
    elif numero > secreto:
        print("El número secreto es menor.")
    else:
        print("¡Felicidades! Adivinaste el número.")
