interes_anual = 1.04
ahorros = float(input("Dinero ahorrado: $"))

primer_ano = round(ahorros * interes_anual, 2)

segundo_ano = round(primer_ano * interes_anual, 2)

tercer_ano = round(segundo_ano * interes_anual, 2)


print("El balance después del primer año: $", primer_ano)

print("El balance después del segundo año: $", segundo_ano)

print("El balance después del tercer año: $", tercer_ano)