squares = [x**2 for x in range(1, 11)]

print(squares)

evens = [x for x in range(1, 21) if x % 2 == 0]

print(evens)


celsius = [0,10,20,30,40]
fahrenheit = [(temp * 9/5) *32 for temp in celsius]
print(fahrenheit)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]


print([[row[i] for row in matrix] for i in range(4)])


#Without comprehension list
transported = []

for i in range(4):
    transported_row = []
    for row in matrix:
        transported_row.append(row[i])
    transported.append(transported_row)

print(transported)