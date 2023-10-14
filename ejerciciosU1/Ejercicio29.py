"""Esto es un comentario."""

nombre = input("Introduce tu nombre: ")

if nombre == "":
    nombre = "Desconocido"
edad = int(input("Introduce tu edad: "))
while edad < 0 or edad > 125:
        edad = int(input('Edad incorrecta. Por favor, introduzca una edad entre 0 y 125: '))

print("Tu nombre es", nombre, "y tu edad es", edad, "años")

tiempovida = 125 - edad
print("Te quedan", tiempovida, "años por cumplir.")