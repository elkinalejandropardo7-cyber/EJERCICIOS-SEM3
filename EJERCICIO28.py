
numero = int(input("Ingresa un número entero positivo: "))
divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores += 1

if divisores == 2:
    print("El número es primo.")
else:
    print("El número no es primo.")
