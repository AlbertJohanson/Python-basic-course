import random
print("Piedra, Papel o Tijera")
print("Seleccione una opcion")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
eleccionPlayer = int(input("Seleccione una opcion: "))
print(f"El Jugador 1 ha elido {eleccionPlayer}")
eleccionCPU = random.randrange(4)
print(f"El CPU ha elido {eleccionCPU}")

if(eleccionPlayer == 1  and eleccionCPU == 2): 
    print("Ha ganado el CPU")
elif(eleccionPlayer == 2 and eleccionCPU == 1):
    print("Ha ganado el Jugador 1")
elif(eleccionPlayer == 3 and eleccionCPU == 2):
    print("Ha ganado el CPU")
elif(eleccionPlayer == 2 and eleccionCPU == 3):
    print("Ha ganado el Jugador 1")
elif(eleccionPlayer == 3 and eleccionCPU == 1):
    print("Ha ganado el CPU")
elif(eleccionPlayer == 1 and eleccionCPU == 3):
    print("Ha ganado el Jugador 1")
else:
    print("Hay un empate")