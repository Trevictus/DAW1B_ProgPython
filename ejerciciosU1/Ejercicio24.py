precioprod = float(input('Di el precio del producto en euros: '))
euros = int(precioprod)
centimos = int(round((precioprod - euros) * 100))

print(f'El precio del producto es {euros} euros y {centimos} céntimos.')