def factorial(num: int):
    total = 1
    while num > 0:
        total*= num
        num -= 1
        return total
    
def factorial(num: int):
    total = 1
    res = str(num) + "! =>"
    while num > 0:
        res += str(num)
        if num != 1:
            res += " x "
        total*= num
        num -= 1
    res += " x " + total
    return res


numero = input("introduce nº: ")
print("Elfactorial de 4  es " + str(factorial(numero)))