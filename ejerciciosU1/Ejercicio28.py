""""
inicio
        Escribe"Dame un numero"
        lee num1
        Escribe"Dame otro"
        lee num2
    si num1 == num2 entonces:
        Escribe "Los numeros no pueden ser iguales"
    sino entonces:
        si num1 < num2 entonces:
            menor = num1
        sino entonces:
            menor = num2
        distancia = valorabsoluto de (num1 - num2) - 1
        Escribe"El nº menor es" + menor + "yentre ellos existen" + distancia + "nºs enteros"

fin
"""


num1 = int(input('Dame un nº: '))
num2 = int(input('Dame otro: '))

if num1 == num2 :
    print('Los numeros no pueden ser iguales.')
else :
    if num1 < num2 :
        menor = num1
    else :
        menor = num2

    distancia = abs(num1 - num2) - 1
    print('El nº menor es', menor, 'y entre ellos existen', distancia, 'nºs enteros.')