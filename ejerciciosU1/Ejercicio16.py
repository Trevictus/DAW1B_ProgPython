
barrapan = float(3.49)
barravendida = barrapan * 0.6 - barrapan

unidtotales = float(input('¿Cuantas barras pasadas has vendido?:'))

print('El precio habitual de una barra de pan es de: ', barrapan)
print('El descuento que se le hace por no ser fresca es de: ', barrapan - barravendida)
print('El coste total de todas las barras no frescas es de: ',barravendida * unidtotales)