stock = 20

while stock > 0:
    print(f"\nStock disponible: {stock}")
    cantidad = int(input("Cantidad a vender: "))

    if cantidad <= 0:
        print("Error: ingrese una cantidad mayor que 0.")
    elif cantidad > stock:
        print("Error: la venta supera las existencias.")
    else:
        stock -= cantidad
        print(f"Venta realizada. Quedan {stock} unidades.")

print("\nStock en 0. Fin del proceso.")