secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
number = int(input("Ingresa el numero secreto:"))

while number != secret_number:
    print("""
              
          ¡Ja, ja! 
        ¡Estás atrapado
          en mi bucle!
              
        """)
    
else:
        print("""
              
        ¡Bien hecho,
        muggle! 
        Eres libre
        ahora.
        """)