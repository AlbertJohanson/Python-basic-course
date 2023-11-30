name = 'Albert'
lastName = 'Johanson'

print(name)
print(lastName)

full_name = name + ' ' + lastName
print(full_name)

quote = "I'm Albert"
print(quote)

quote2 = ' She said "Hello" '
print(quote2)


# format 
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, lastName)
print(template)

template2 = f"Hola, mi nombre es {name} y mi apellido es {lastName}"
print(template2)