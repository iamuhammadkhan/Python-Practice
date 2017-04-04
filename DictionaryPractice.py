students = {'Eric': 26, 'Tina': 24, 'Bob': 30}
print(students)
print(students['Bob'])
students['Bob'] = 25
print(students['Bob'])

del students['Bob']
print(students)
print(students)
print(len(students))
print(students.keys())
print(students.values())

students.clear()

del students

tup1 = ('Maths', 30, 'Help')
print(tup1)

tup1 = ('Cheese')
print(tup1)

tup1 = ('Maths', 30, 'Help')
print(tup1[1])
print(tup1[0:2])

del tup1
