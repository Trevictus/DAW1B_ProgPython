num1 = float(input('Introduce la cantidad a depositar: '))
año1 = (num1 * 0.04 + num1)

año2 = (año1 + (año1 * 0.04))

año3 = (año2 + (año2 * 0.04))

print('La cantidad de ahorros en el primer año asciende a:',"{0:.2f}". format(float(año1)))
print('La cantidad de ahorros en el segundo año asciende a:',"{0:.2f}". format(float(año2)))
print('La cantidad de ahorros en el tercer año asciende a:',"{0:.2f}". format(float(año3), "unidades."))

