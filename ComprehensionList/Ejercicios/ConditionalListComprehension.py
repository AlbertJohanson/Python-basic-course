numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


sequence = [x * 2 if x % 2 == 0 else x for x in numbers]
print(sequence)