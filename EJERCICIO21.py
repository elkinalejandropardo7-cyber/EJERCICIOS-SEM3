
presentes = 0
ausentes = 0

while True:
    letra = input("Ingresa P (Presente), A (Ausente) o F (Fin): ").upper()

    if letra == "P":
        presentes += 1
    elif letra == "A":
        ausentes += 1
    elif letra == "F":
        break
    else:
        print("Opción no válida.")

print("Total de presentes:", presentes)
print("Total de ausentes:", ausentes)
