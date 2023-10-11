num1 = int(input('Dame un nº: '))
num2 = int(input('Dame otro: '))

if num1 == num2 :
    print('Los numeros no pueden ser iguales.')
    int(input('Dame un nº: '))
    int(input('Dame otro: '))
elif num1 < num2 :
    print('el nº menor es ', num1, '.' )
elif num1 > num2 :
    print('el nº menor es ', num2, '.')