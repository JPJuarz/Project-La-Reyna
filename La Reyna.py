# Inicializando listas para las órdenes
drinks = []
comidas = []

# Definición de precios como listas de listas
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

print("Bienvenidos a La Reyna")

# Función para ordenar las bebidas
def order_drinks():
    drinksqacorrect = ["Si", "si", "Sí", "sí", "S", "s", "Y", "y"]
    while True:
        drinksqa = input("¿Les gustaría ordenar algo para beber? ")
        if drinksqa in drinksqacorrect:
            while True:
                numdrink = int(input("¿Cuántas bebidas desea? "))
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
def order_food():
    foodqacorrect = ["Si", "si", "Sí", "sí", "S", "s"]
    while True:
        foodqa = input("¿Les gustaría ordenar algo para comer? ")
        if foodqa in foodqacorrect:
            while True:
                numcomida = int(input("¿Cuántas comidas desea? "))
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

# Llamando las funciones
order_drinks()
order_food()

# Extras
extras = []
extrasansw = ["Si", "si", "Sí", "sí", "S", "s", "Y", "y"]
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
def preciototal():
    total = 0
    for drink in drinks:
        for item in drinks_info:
            if drink == item[0]:
                total += item[1]
    for food in comidas:
        for item in food_info:
            if food == item[0]:
                total += item[1]
    return total

# Orden final
total = (preciototal())
recibo = " 1 ".join(drinks + comidas)
print("Su orden es:", recibo, extras)
print("El precio total de su pedido sería: $", total)