amigos = ["Juan", "Pedro", "Maria", "Marta"]
print("Amigos: ", amigos)
amigos.extend(["Marcos", "Sofia"])
print("Conocimos nuevos amigos: ", amigos)
amigos.append("Pablo")
print("Llegò un amigo màs: ", amigos)
amigos.remove("Pablo")
print("Pablo no fue de nuestro agrado ", amigos)

alfredo = "Alfredo"

if alfredo in amigos:
    print("Si conocemos a Alfredo")
else:
    print("No conocemos a Alfredo")

amigos.sort()
print("Amigos en orden alfabètico: ", amigos)

print("Primero 3 amigos: ", amigos [:3])

ubicacion_pedro = amigos.index("Pedro")

print("Pedro està ubicado en la posiciò: ", ubicacion_pedro)