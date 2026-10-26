deuda = float(input("Valor de la deuda: "))
meses = int(input("Meses en mora: "))

mes = 1
while mes <= meses:
    deuda = deuda * 1.05
    print(f"Mes {mes}: ${deuda:,.2f}")
    mes += 1

print(f"\nSaldo final adeudado: ${deuda:,.2f}")