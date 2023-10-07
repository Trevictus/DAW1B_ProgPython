pesopayasos = 0.112
pesomuñecas = 0.075

numpayasos = int(input('Introduce el numero de payasos vendidos: '))
nummuñecas = int(input('Introduce el número de muñecas vendidas: '))

print('El peso del paquete a enviar será de:', numpayasos * pesopayasos + pesomuñecas * nummuñecas, 'kg')