"""
Proyecto La Reyna
Simulador de un menu virtual sobre un restaurante
El programa le pregunta al usuario si este desearía ordenar bebidas y comidas y
si este es el caso, el usuario decide cuantas de cada una quiere y después
son desplegadas las opciones  disponibles. El usuario decide cuales de estas opciones
son las que le gustarían agregando a listas sus pedidos y los precios de estos.
Al final entrega su orden junto con el precio total de está.
"""

"""
======== Funciónes para la orden del usuario ========
"""

# Función para ordenar las bebidas
def order_drinks(drinksqacorrect, drinksqa, numdrink):
    """
    (Uso de condicionales, operadores, listas, listas anidadas, ciclos, ciclos anidados, variables)
    Recibe: las respuestas aceptadas para correr la función, la respuesta de la pregunta
    al usuario sobre si desea bebidas, el número de bebidas deseadas
    Checa si esta la respuesta en las respuestas aceptadas, hace un ciclo para el número de
    bebidas deseadas donde imprime las bebidas disponibles junto con su precios en el formato
    deseado, pregunta cual o cuales bebida quiere el usuario, las agrega a la lista de
    bebidas e imprime la orden de bebidas
    Devuelve: las bebidas deseadas en la lista (sin imprimir), la orden del usuario
    """
    while True:
        if drinksqa in drinksqacorrect:
            while True:
                if numdrink > 0:
                    break
                else:
                    print("Por favor, ingrese un número mayor a 0.")
            for i in range(numdrink):
                print("Opciones de bebidas:")
                for drink in drinks_info:
                    print("{} - ${}".format(drink[0], drink[1]))
                drink = input("Por favor ordene una bebida: ")
                drinks.append(drink)
            print("Perfecto, su orden de bebidas es:", drinks)
            break
        else:
            drinks.append("ninguna bebida")
            print(drinks)
            break

# Función para ordenar comida
def order_food(foodqacorrect, foodqa, numcomida):
    """
    (condicionales, operadores, listas, listas anidadas, ciclos, ciclos anidados, variables)
    Recibe: las respuestas aceptadas para correr la función, la respuesta de la pregunta
    al usuario sobre comida, el número de comidas deseadas
    Checa si la respuesta dada esta en las respuestas aceptadas, hace un ciclo para las
    comidas deseadas donde imprime las comidas disponibles junto con sus precios
    en el formato deseado, pregunta cual o cuales comidas quiere el usuario, las agrega a
    la lista de comidas e imprime la orden
    Devuelve: las comidas deseadas en la lista (sin imprimir), la orden del usuario
    """
    while True:
        if foodqa in foodqacorrect:
            while True:
                if numcomida > 0:
                    break
                else:
                    print("Por favor, ingrese un número mayor a 0.")
            for i in range(numcomida):
                print("Opciones de comida:")
                for comida in food_info:
                    print("{} - ${}".format(comida[0], comida[1]))
                food = input("Por favor ordene una comida: ")
                comidas.append(food)
            print("Perfecto, su orden de comidas es:", comidas)
            break
        else:
            comidas.append("ninguna comida")
            print(comidas)
            break

# Función para ordenar extras
def order_extras(extrasansw):
    """
    (condicionales, operadores, listas, listas anidadas, ciclos, variables)
    Recibe: Las respuestas aceptadas de la pregunta sobre extras para seguir con la función
    Pregunta cuales de las comidas extra le gustaría al usuario, añade a la lista si
    le gustaría cada uno (aguacate, salsa, cebollla) en especifico o no
    Devuelve: cuales extras le gustarían al usuario dentro de la lista - extras
    """
    while True:
        extrasagu = input("¿Les gustaría añadir aguacate a su pedido? ")
        if extrasagu in extrasansw:
            extras.append("con aguacate")
            break
        else:
            extras.append("sin aguacate")
            break

    while True:
        extrassals = input("¿Les gustaría añadir salsa a su pedido? ")
        if extrassals in extrasansw:
            extras.append("con salsa")
            break
        else:
            extras.append("sin salsa")
            break
    
    while True:
        extrasceb = input("¿Les gustaría añadir cebolla a su pedido? ")
        if extrasceb in extrasansw:
            extras.append("con cebolla")
            break
        else:
            extras.append("sin cebolla")
            break
        
# Función que calcula precio total
def preciototal(drinks, comidas):
    """
    (Ciclos, ciclos anidados, funciones, listas, listas anidadas, operadores, aritmética, matrices)
    Recibe: Los valores añadidos por las previas funciones de ambas listas (drinks y comida)
    o puesto de otra manera de otra manera, la orden del usuario
    Agrega un total de precio que empieza en cero, checa  cada una de las ordenes del usuario
    comparandolas con las matrices, si coinciden le agrega al total el precio / número que tiene
    designado esa comida o bebida
    Devuelve: El precio total de la orden del usuario
    """
    total = 0
    for drink in drinks:
        for i in drinks_info:
            if drink == i[0]:
                total += i[1]
    for food in comidas:
        for i in food_info:
            if food == i[0]:
                total += i[1]
    return total

"""
======== PARTE PRINCIPAL DEL PROGRAMA ========
"""

# Inicializando listas para las órdenes
drinks = []
drinksqacorrect = ["Si", "si", "Sí", "sí", "S", "s", "Y", "y"]
comidas = []
foodqacorrect = ["Si", "si", "Sí", "sí", "S", "s"]
extras = []
extrasansw = ["Si", "si", "Sí", "sí", "S", "s", "Y", "y"]

# Definición de precios como listas de listas / matrices
drinks_info = [["Agua", 30],
["Refresco", 50],
["Jugo", 50],
["Agua del Día", 60],
["Licuado", 80],
["Malteada", 90]]

food_info = [["Torta de Milanesa", 90],
["Torta de Milanesa con queso", 100],
["Torta de Pierna", 90],
["Torta de Pierna con queso", 100],
["Torta de Chile Relleno", 90],
["Torta de Jamón y Queso", 80],
["Torta de Carne", 90]]

#Preguntas para correr las funciones
print("Bienvenidos a La Reyna")
drinksqa = input("¿Les gustaría ordenar algo para beber? ")
if drinksqa in drinksqacorrect:
    numdrink = int(input("¿Cuántas bebidas desea? "))
    order_drinks(drinksqacorrect, drinksqa, numdrink)

foodqa = input("¿Les gustaría ordenar algo para comer? ")
if foodqa in foodqacorrect:
    numcomida = int(input("¿Cuántas comidas desea? "))
    order_food(foodqacorrect, foodqa, numcomida)

if foodqa in foodqacorrect:
    order_extras(extrasansw)

# Orden final
total = preciototal(drinks, comidas)  
recibo = " 1 ".join(drinks + comidas)
extrasj = " , ".join(extras)
print("Su orden es:", recibo, "/", extrasj)
print("El precio total de su pedido sería: $", total)