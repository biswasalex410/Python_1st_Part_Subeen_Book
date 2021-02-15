'''
def add_numbers(numbers):
    result = 0
    for number in numbers:
        result += number
    return result
result = add_numbers([1, 2, 30, 6, 6, 9])
print(result)

def test_fnc(li):
    li[0] = 10

my_list = [1, 2, 3, 4]
print("before function call", my_list)
test_fnc(my_list)
print("after function call", my_list)

'''

list1 = [1, 2, 3, 4]
list2 = list1
print(list1)
print(list2)
list2[0] = 100
print(list2)
print(list1)

li = [1, 2, 3]
result = sum(li)
print(result)