"""
inicio
    Escribee "introduce un nº"
    lee numini
    Escribe "introduce el nº de incremento"
    lee incremento
    mientras incremento < 0 hacer:
        Escribe "el nº del incremento no puedee ser negativo"
        lee incremento
        Escribe "introduce de nuevo el nº de incremento"
        lee incremento
    Esccribe "introduce donde tiene que llegar la serie"
    lee total
    mientras total< 0 hacer:
        Escribe" el nº del total no puede ser neegativo"
        lee total
        Escribe "introduce de nuevo el nº para el total"
        lee total
    para i en rango (numini, total+1, incremento)
        si i es igual a numini entonces:
            concatena la variable + i + "-"
        y si i es igual a total-incemento entonces:
            concatena la variable + i + "-"
        sino:
            concatena la variable + i + ".."
    Escribe la variable.
fin
"""
numini = int(input("Introduce un nº: "))

incremento = int(input("Introduce un nº para el incremento: "))
while incremento < 0 :
    print ("El nº del incremento no puede ser negativo")
    incremento = int(input("Introduce de nuevo el nº para el incremento: "))

total = int(input("Introduce hasta donde tiene que llegar la serie: "))
while total < 0 :
    print ("El nº del total no puede ser negativo")
    total = int(input("Introduce de nuevo el nº para el total: "))
variable = str("Serie => ")
for i in range(numini, total + 1, incremento):
    if i == numini :
        variable += repr(i)+ "-"
    
    elif i == total-incremento:
        variable += repr(i)+ "-"
    else:
        variable +=repr(i)+ ".."
print(variable)