total = 0
precio = float(input("Precio del producto (0 para terminar): "))

while precio != 0:
    total += precio
    precio = float(input("Precio del producto (0 para terminar): "))

print(f"\nTotal a pagar: ${total:,.0f}")