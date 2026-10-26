
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

while num2 != 0:
    residuo = num1 % num2
    num1 = num2
    num2 = residuo

print("El MCD es:", num1)
