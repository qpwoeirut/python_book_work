students1 = ['Giacomo', 'Ava', 'Ely', 'Andrew', 'Leena', 'Tyler', 'Peter', 'Neo', 'Sophie', 'Kaashika', 'Pablo', 'Talya', 'Marvin', 'Jacob', 'Willow', 'Karen', 'Alexis', 'Jonathan', 'Anthony', 'Jada', 'Stanley']
students2 = ['Giacomo', 'Ava', 'Ely', 'Andrew', 'Leena', 'Tyler', 'Peter', 'Neo', 'Sophie', 'Kaashika', 'Pablo', 'Talya', 'Marvin', 'Jacob', 'Willow', 'Karen', 'Alexis', 'Jonathan', 'Anthony', 'Jada', 'Stanley']
absent = students1.pop(1), students1.pop(1), students1.pop(1), students1.pop(7), students1.pop(7), students1.pop(10)

print('Room 8 Attendance')
for idx, val in enumerate(students1):
    print(val, 'is present.')


for idx, val in enumerate(absent):
    print(val, 'is absent.')


print(len(students1), 'students are present.')
print(len(absent), 'students are absent.')
print(len(students2), 'students total.')