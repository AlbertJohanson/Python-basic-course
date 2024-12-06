numbers = {
    1: "uno",
    2: "dos",
    3: "tres"
}

print(numbers[2])

information = {
    "nombre" : "Albert",
    "apellido": "Trujillo",
    "edad": 24,
    "altura": 188
}
print(information)
del information["edad"]
print(information)

#Metodo keys
claves = information.keys()
print(type(claves))
print(claves)

#Metodo Values
values = information.values()
print(values)

#Metodo items
pairs = information.items()
print(pairs)

contacts = information = {
    "Albert" :{"apellido": "Trujillo",
    "edad": 24,
    "altura": 188}, 
     "Wendoly": {
    "apellido": "Gisell",
    "edad": 22,
    "altura": 177},
     "Chelsea": {
    "apellido": "Rizo",
    "edad": 18,
    "s.altura": 160}
}

print(contacts["Chelsea"])



