
blocks = int(input("Ingresa el número de bloques: "))
blocks_need = 1
height = 0
while blocks >= blocks_need:
    blocks -= blocks_need
    height += 1
    blocks_need += 1
    

print("La altura de la pirámide:", height)
