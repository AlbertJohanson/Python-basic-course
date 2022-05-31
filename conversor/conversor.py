menu = """" 
Welcome to the converter!   

    1. Quetzales to dollars 
    2. Quetzales to euros
    3. Quetzales to pesos

Choose one option: """


option = input(menu)


if option == "1":
    quetzales = input("How many quetzales do you have?: ")
    quetzales = float(quetzales)
    value_dóllars = 7.67
    dóllars = quetzales / value_dóllars
    dóllars = round(dóllars, 2)
    dóllars = str(dóllars)
    print("You have $" + dóllars + " dóllars")
elif option == "2":
    quetzales = input("How many quetzales do you have?: ")
    quetzales = float(quetzales)
    value_euros = 8.21
    euros = quetzales / value_euros
    euros = round(euros, 2)
    euros = str(euros)
    print("You have €" + euros + " euros")
elif option == "3":
    quetzales = input("How many quetzales do you have?: ")
    quetzales = float(quetzales)
    value_pesos = 0.39
    pesos = quetzales / value_pesos
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print("You have $" + pesos + " pesos mexicans")
else:
    print("Please choose a valid option")




# quetzales = input("¿Cuántos quetzales tienes?: ")
# quetzales = float(quetzales)
# valor_dolar = 7.67
# dolares = quetzales / valor_dolar
# dolares = round(dolares, 2)
# dolares = str(dolares)
# print("Tienes $" + dolares + " dólares")


# # Dolares a quetzales
# dolares = input("¿Cuántos dólares tienes?: ")
# dolares = float(dolares)
# valor_quetzales = 0.13
# quetzales = dolares / valor_quetzales
# quetzales = round(quetzales, 2)
# quetzales = str(quetzales)
# print("Tienes " + quetzales + " quetzales")