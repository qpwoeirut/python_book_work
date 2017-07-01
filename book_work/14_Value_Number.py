for value in range(0,9):
    print(value)

for number in range(8,9):
    print(number)

sequence = list(range(1,11))
print(sequence)

squares = []
for value in range(1,11):
    squares.append(value **2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

cubes = [val **3 for val in range(1,1001)]
print(cubes)