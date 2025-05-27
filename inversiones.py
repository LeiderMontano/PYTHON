dinero = float(input("Cuanto dinero desea invertir: $"))
interes_anual = float(input("Su interes anual: %"))
numero_anos = int(input("Nùmero de años: "))

capital = dinero * (1 + interes_anual / 100) ** numero_anos

print("El capital obtenido es: $" + str(round(capital, 2)))