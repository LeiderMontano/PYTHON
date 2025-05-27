#ASIGNAURAS

asignaturas = ["Matenaticas", "Fisica", "Quimica", "Historia", "Lengua", "Mùsica"]
asignaturas.reverse()

asignaturas.insert(2,"ingles")

print(asignaturas)

musica_esta = "Mùsica"

if musica_esta in asignaturas:
    print("Mùsica si se encuentra en la lista")
else:
    print("Asignatura Mùsica no se encuentra en la lista")