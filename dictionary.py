'''

# student er marks amra avabe list kore rakhte pari

marks = [78, 72, 68, 80, 63, 75, 77, 90]
roll = input("please enter your roll number: ")
print("Your marks is", marks[int(roll)-1])

'''

'''
# sokol student er english o banglar marks rakhar jonno

marks = [[73, 78], [70, 74], [87, 64], [76, 69]]
print(marks[0])
print(marks[1])
print(marks[1][0])

'''

'''
# using dictionary key valu : amra jodu bangla exam er marks gulo dictionary te rakhi

marks = {1: 77, 2: 76, 5: 62, 4: 78, 3: 65}
print(type(marks))
print(marks[3])
print("Marks of roll number 4 is", marks[4])

'''

'''
# kono order ba indexing nai just using key and its value

marks = {1001: 75, 1002: 79, 10521: 90, 1222: 85}
print(marks[10521])

'''

'''
# roll no digit na hole o problem nai

marks = {"DIU201": 75, "DIU855": 76, "DIU889":96, "DIU774":73}
print(marks["DIU889"])

'''

'''
# we can make blank dictionary then we can add key and value

dt = {}
print(dt)
print(type(dt))
dt[1] = "one"
print(dt)
dt[2] = "two"
print(dt)
dt[3] = "three"
print(dt)

'''

'''

# kono key jodu dictionary te na thake tahole amra set access korar somoy python error dibe

dt = {"a": "A", "b": "B", "c": "C"}
print(dt["a"])
print(dt["b"])
print(dt["c"])
dt["d"] = "D"
print(dt["d"])

'''

'''

# mutable noy amon kisu use kora jay.
dt = {"a": "A", "b": "B", "c": "C"}
dt [(1, 2, 3)] = "tuple"
print(dt)

s = {1, 2, 3}
print(s)
print(type(s))

'''

'''

# exercise dictionary use kore bivinno student er bangla o english er marks avabe rakhte pari

marks = {"SANAT": {"Bangla": 75, "English": 80}, "ALEX": {"Bangla": 77, "English": 79}}
print(marks)

'''



# Big example of dictionary

bd_division_info = {}
bd_division_info["Barishal"] = {"district": 6, "upazila": 39, "union": 330}
bd_division_info["Chittagong"] = {"district": 11, "upazila": 97, "union": 336}
bd_division_info["Dhaka"] = {"district": 13, "upazila": 93, "union": 1833}
bd_division_info["Khulna"] = {"district": 10, "upazila": 59, "union": 270}
bd_division_info["Mymensingh"] = {"district": 4, "upazila": 34, "union": 350}
bd_division_info["Rajshahi"] = {"district": 8, "upazila": 70, "union": 558}
bd_division_info["Rangpur"] = {"district": 8, "upazila": 58, "union": 536}
bd_division_info["Sylhet"] = {"district": 4, "upazila": 38, "union": 334}
print(bd_division_info)
divisions = bd_division_info.keys()

'''

# loop diye ekti ekti bivag print korbo

divisions = bd_division_info.keys()
print(divisions)
for division in divisions:
    print("Division", division)

'''

'''

# protiti bivage koyti district + upozila ase ta ber korbo loop use kore

for division in divisions:
     print(division, "District:", bd_division_info[division]["district"], "Upazila:", bd_division_info[division]["upazila"])
'''

'''

# amra jodi sorasori dictionary er upor loop chalai tahole kebol key gula pabo
for item in bd_division_info:
    print(item)
    
'''

# amra jodi key o vvalue dutoi pete chai tahole amdr 2i method asee
# 1st method

''''
for key in bd_division_info:
    print(key)
    print(bd_division_info[key])

'''

# 2nd method

'''

for key, value in bd_division_info.items():
    key += key
    print(key)
    print(value)
    
'''

#