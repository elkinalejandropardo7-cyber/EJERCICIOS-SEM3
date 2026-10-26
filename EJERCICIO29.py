
numero = int(input("Ingresa un número entero: "))
numero = abs(numero)
suma = 0

while numero > 0:
    digito = numero % 10
    suma = suma + digito
    numero = numero // 10

print("La suma de los dígitos es:", suma)
