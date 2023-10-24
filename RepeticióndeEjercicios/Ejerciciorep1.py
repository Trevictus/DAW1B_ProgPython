#Programa que te dá la bienvenida preguntandote por tu estado anímico#
def chistes(chiste1, chiste2):
    chiste1 = "Estando un pintor aburrido y sin trabajo, en un mural empezó a pintar la Luna, y del hambre que tenía, pintó un plato de aceitunas."
    chiste2 = "Va una canina a un bar y pide un vaso de cerveza y una fregona exprimida..."
    print(chiste1 + chiste2)






nombre = input("--¿Cual es tu nombre?\n")
print("--¡Buenas!, ", nombre, "¿Que tal estás hoy? ¿Bien, mal o regular?")
estado = input()
if estado == "Bien" or estado == "bien":
    print("--¡Me alegro mmucho!")
elif estado == "Mal" or estado == "mal":
    print("--No te preocupes porque la vida es así.")
elif estado == "Regular" or estado == "regular":
    print("--Al menos, me alegro que hables conmigo.")
else:
    print("--JAJAJAJA, no sé qué estado de anímico es ese.")
    print("--Aunque me haya reido, perdóname, no sé que problemas puedes tener.")


respuesta = input("¿Quiereees oir un chiste?\n")
chiste = "Estando un pintor aburrido y sin trabajo, en un mural empezó a pintar la Luna, y del hambre que tenía, pintó un plato de aceitunas."

chiste2 = "Va una canina a un bar y pide un vaso de cerveza y una fregona exprimida..."
if respuesta == "Si" or respuesta == "si":
    print(chiste)
else:
    print("Lo siento cabesa no to el mundo puede ser de Cai. ¿Quieres que te alegre el momento? ¿Si o no?.")
    respuesta2 = input()
    if respuesta2 == "Si" or respuesta2 == "si":
        print(chiste2)
    elif respuesta2 =="No" or respuesta2 == "no":
        print("No te preocupes ya te dejo.")
    

