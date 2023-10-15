"""
Inicio

	Escribe "Introduce un número: "
	Lee x
	Escribe "Introduce otro: "
	Lee y
	
	Si (x <= y) entonces
		numIni = x
		numFin = y
	Sino
		numIni = y
		numFin = x
		
	Mientras (numIni <= numFin) hacer
		Escribe numIni
		Si (numIni != numFin) entonces
			Escribe "-"
                numIni = numIni + 1

Fin
"""

x = int(input("Introduce un nº: "))
y = int(input("Introduce otr: "))

if (x <= y):
    numini = x
    numfin = y
else:
    numini = y
    numfin = x
while (numini <= numfin):
    print (numini, end = "")
    if (numini != numfin):
        print("-", end = "")
    numini = numini + 1
