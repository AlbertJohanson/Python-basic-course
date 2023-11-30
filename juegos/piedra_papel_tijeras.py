import os 
os.system('clear')

eleccion = input('¿Piedra, papel o tijeras?: ').capitalize()

if eleccion == 'Papel':

    print('Computadora elige tijeras. Gana la computadora')

elif eleccion == 'Piedra':

    print('Computadora elige papel. Gana la computadora')

elif eleccion == 'Tijeras':

    print('Computadora elige piedra. Gana la computadora')

else:
    print('Eleccion no valida')