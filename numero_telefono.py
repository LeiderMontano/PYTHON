telefono = input("Dinos el codigo de pais de tu telèfono (Ejemplo: +34-913724710-56) --->")

numero_sin_prefijo_extension = telefono[4:-3]

print("El teléfono es:", numero_sin_prefijo_extension)