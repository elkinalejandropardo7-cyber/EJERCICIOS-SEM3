saldo = 500000

while saldo > 0:
    print(f"\nSaldo disponible: ${saldo:,.0f}")
    retiro = float(input("Valor a retirar (0 para salir): "))

    if retiro == 0:
        break
    elif retiro < 0:
        print("Error: ingrese un valor válido.")
    elif retiro > saldo:
        print("Error: el retiro supera su saldo.")
    else:
        saldo -= retiro
        print("Retiro exitoso.")

print(f"\nTransacción finalizada. Saldo restante: ${saldo:,.0f}")