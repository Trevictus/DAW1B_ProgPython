"""Esto es un comentario."""

nombre = str(input('Introduce tu nombre: '))
edad = int(input('Introduce tu edad: '))

if nombre == None :
    print('!!!DESCONOCIDO!!!')
    int(input('Introduce tu edad entre 0 y 125 :', 0 > edad <= 125))
if nombre == nombre :
    print('Te llamas ', nombre, 'y te quedan ', 125 - edad, 'por cumplir.')