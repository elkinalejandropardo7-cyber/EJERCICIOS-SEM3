
maximo = None

while True:
    numero = int(input("Ingresa un número (0 para terminar): "))

    if numero == 0:
        break

    if maximo is None or numero > maximo:
        maximo = numero

if maximo is None:
    print("No ingresaste ningún número.")
else:
    print("El número más alto es:", maximo)