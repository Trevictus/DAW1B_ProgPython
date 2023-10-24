def suma(num1, num2):
    return num1 + num2










print(suma(3, 2))
print("La suma de", 3, "+", 2, "es", suma(3, 2))
print("La suma de " + str(3) + " + " + str(2) + " es " + str(suma(3, 2)))
resultado = "La suma de "
resultado += str(suma(3,2))
resultado += " + " + str(suma(2))
resultado += " es " + str(suma(3, 2))
print(resultado)
print(f"La suma de {3} + {2} es {suma(3, 2)}")