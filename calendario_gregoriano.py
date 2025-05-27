year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
    if (year % 4) != 0:
        print("Año comùn")
    elif (year % 100) != 0:
        print("Año bisiesto")
    elif (year % 400) != 0:
        print("Año comùm")
    else:
        print("Año bisiesto")
    #  Escribe el bloque if-elif-elif-else aquí.