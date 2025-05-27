frase = input("Escribe una frase: ")
vocal = input("Escribe una vocal en minusculas: ")

if len(vocal) != 1 or vocal not in "aeiou":
    print("Error: Debes escribir una sola vocal en minusculas.")
else:
    frase_modificada = frase.replace(vocal, vocal.upper())
    
    print("Frase con la vocal en mayùscula:", frase_modificada)