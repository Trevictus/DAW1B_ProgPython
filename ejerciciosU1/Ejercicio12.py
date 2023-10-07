kg = float(input('Introduce tu peso en kg: '))
m = float(input('introduce tu estatura en metros: '))

IMC = (kg / (m * m))

print('Tu índice de masa corporal es: ', "{0:.2f}".format(float(IMC)))