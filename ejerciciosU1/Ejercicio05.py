imp = float(input("importe del articulo: "))
iva = float(input("% de IVA: "))

impIVA = imp * (1 + iva / 100)

print(impIVA)