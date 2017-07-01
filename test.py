from random import randint

v = 0

qwerty = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)

for num in qwerty:
    if num % 2 == 0:
        v = v + num

print(qwerty)
print(v)