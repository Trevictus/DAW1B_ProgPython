"""
Escribe un algoritmo en pseudocódigo que lea un número y te diga si es par o impar.
El número no puede ser negativo ni mayor de 10, en tal caso solo mostrará un mensaje de error.
"""

"""
Inicio
    Escribe "introduce un nº entre 0 y 10"
    Lee num1
    Si (num1 < 0 o num1 >10) entonces:
        Escribe "Error, debes introducir un nº entre 0 y 10."
    Sino entonces:
        si (num1 == 1 o num == 3 o num == 5 o num == 7 o num == 9) entonces:
            Escribe "El nº introducido es impar."
        sino:
            Escribe "El nº introducido es par.


Fin
"""

num = int(input("introduce un nº entre el 0 y el 10: "))

if (num < 0 or num > 10):
    print("Error, debes introducir un nº entre 0 y 10.")

else:
    if num in [1,3,5,7,9]:
        print("El nº introducido es impar.")
    else:
        print("El nº introducido es par.")
