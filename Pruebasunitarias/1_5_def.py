

def precio_coniva(total):
    importe=float(input("Precio del articulo: "))
    iva=float(input("% Impuesto a aplicar : "))
    total = (importe * iva) / 100
    print("El precio del articulo con iva es ", total, ".")






imp = float(input("importe del articulo: "))
iva = float(input("% de IVA: "))
total = (imp*iva)/100
print(total)