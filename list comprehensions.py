#using normal mood

li = [1, 2, 3]
new_li = []
for x in li:
    new_li.append(2 * x)
print(new_li)

#comprehensions mood

new_li = [2 * x for x in li]
print(new_li)

# without function

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = []
for x in  li:
    if x % 2 == 0:
        even_number.append(x)
print(even_number)

# using comprehemsions function

even_numbers = [x for x in range(1,11) if x % 2 == 0]
print(even_numbers)