#Crear un iterador para los numeros impares

#Limite
limit = 100

#Crear Iterador
odd_iterator = iter(range(0,limit+1,2))

#Usar el iterador
for num in odd_iterator:
    print(num)