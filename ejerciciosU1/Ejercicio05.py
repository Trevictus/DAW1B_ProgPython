

def precio(imp: float, iva: float):

    impIVA = imp * (1 + iva / 100)
    return round(impIVA,2)

imp = float(input("importe del articulo: "))
iva = float(input("% de IVA: "))
variable = precio(imp,iva)
print(variable)