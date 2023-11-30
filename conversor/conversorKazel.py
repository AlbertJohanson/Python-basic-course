import os 
os.system('clear')

USD = 1
Q = 7
ARS = 230
MXN = 17

print("===== Bienvenido al Conversor de Monedas =====")

print("Elige una de las siguientes opciones: ")

print("1. Quetzales")
print("2. Pesos Argentinos")
print("3. Pesos Mexicanos")

opcion = int(input("Ingresa una opción: "))





if opcion == 1:
    dolares = int(input("Ingresa la cantidad de dolares:"))
    quetzales = dolares * Q
    print(f"La cantidad de quetzales es: {quetzales}")
elif opcion == 2:
    dolares = int(input("Ingresa la cantidad de dolares:"))
    pesos_argentinos = dolares * ARS
    print(f"La cantidad de pesos argentinos es: {pesos_argentinos}")
elif opcion == 3:
    dolares = int(input("Ingresa la cantidad de dolares:"))
    pesos_mexicanos = dolares * MXN
    print(f"La cantidad de pesos mexicanos es: {pesos_mexicanos}")
else:
    print("Ingresa una opción correcta por favor")
    exit()