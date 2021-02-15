#saarc = ["Bangladesh", "India", "Sri Lanka", "Pakistan", "Nepal", "Bhutan"]
#print(saarc)

#saarc.append("Afganistan")
#print(saarc)



# list mutebale  + sorting list value

#saarc.sort()
#print(saarc)

#li = [1, 2, 8, 6, 0]
#li.sort()
#print(li)

#reverse method

#li = [1, 2, 6, 3, 9, 5]
#li.sort()
#li.reverse()
#print(li)

#li = ["mango", "banana", "orange"]
#print(li)

# inserting

#fruits = ["mango", "banana", "orange"]
#fruits.insert(1, "apple")
#print(fruits)

# removing

#fruits = ["mango", "apple", "banana", "orange"]
#fruits.remove("apple")
#print(fruits)

# pop methhod

fruits = ['apple', 'mango', 'banana', 'orange']
item = fruits.pop(1)
print(item)
print(fruits)

# add list after list

li = [1, 2, 3]
li2 = [4, 5, 6]
li.extend(li2)
print(li)

# count method

li =  [1, 2, 3, 3, 4, 5]
print(li.count(3))

print(li.count(5))

print(li.count(10))

#delete list or list element

li = [1, 2, 3, 4, 5]
del(li[3])
print(li)
del(li[0])
print(li)
