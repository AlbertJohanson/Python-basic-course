def converter(type_currency, value_dolar):
    currency = input("How many " + type_currency +" do you have?: ")
    currency = float(currency)
    dollars = currency / value_dolar
    dollars = round(dollars, 2)
    dollars = str(dollars)
    return print("You have $" + dollars + " dóllars")

menu = """" 
Welcome to the converter!   

    1. Quetzales to Dollars 
    2. Euros to Dollars
    3. Yuan to Dollars

Choose one option: """


option = input(menu)


if option == "1":
    converter("quetzales", 7.67)
elif option == "2":
    converter("Euros", 1.07)
elif option == "3":
    converter("Yuan", 0.15)
else:
    print("Please choose a valid option")

