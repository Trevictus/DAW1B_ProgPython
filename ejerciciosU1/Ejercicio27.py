producto = input('Introduce el nombre del producto: ')
precio = float(input('Introduzaca ahora su precio: '))
unidades = int(input('Cuantas unidades: '))
total = precio * unidades

print(f'{producto}: {precio: 6.2f} euros *{unidades : 03d} unidades = {total : 8.2f} euros')