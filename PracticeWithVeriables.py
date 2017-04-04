firstName = 'Muhammad'
lastName = 'Khan'
fullName = firstName + ' ' + lastName
message = 'My name is '
newMessage = ' and my age is '
myAge = 30
print(message + fullName + newMessage + str(myAge))

newName = 'Muhammad Khan asasasasasasasasasasasasasas'

print(newName[0:13])
print(newName[:13])
print(newName[14:])

shoppingList = 'eggs, carrots, milk, cherries, apples'
print(shoppingList)

shoppingList2 = ['eggs', 'milk', 'apples', 'carrots', 'cherries']
print(shoppingList2)
print(shoppingList2[1])
print(shoppingList2[4])
print(shoppingList2[2])
shoppingList2[2] = 'chocolates'
print(shoppingList2[2])
shoppingList2.append('apples')
print(shoppingList2)
print(shoppingList2[5])
del shoppingList2[5]
print(shoppingList2)

array1 = [2, 4, 6, 8,]
array2 = [1, 3, 5, 7, 9]
print(array1)
print(array2)

array3 = array1 + array2
print(array3)
print(len(array3))
print(max(array3))
print(min(array3))

print(shoppingList2.count('chocolates'))
print(shoppingList2.count('apples', 'carrots'))
shoppingList2.append('apples')
print(shoppingList2)
print(shoppingList2.count('apples', 'carrots'))