A = set()
print(A)
print(type(A))

# amra kichu upadan diye set toiri korbo

items = {"pen", "laptop", "cellphone"}
print(items)
print(type(items))

#list ba tuple diye set toiri kora jay

li = [1, 2, 3, 4]
tpl = (1, 2, 3)
A = set(li)
print(A)
B = set(tpl)
print(B)
print(type(A))
print(type(B))

# string theke o set toiri kora jay don't care order or sorting

A = set("Bangladesh")
print(A)
print(type(A))

B = set("Sri Lanka")
print(type(B))
print(B)

# kono jinis set er sodosso kina ta ber korte pari avabe:

A = (1, 2, 3)
print(1 in A)
print(2 in A)
print(5 in A)

# set er nana rokom operation

A = {1, 2, 3, 4, 5}
B = {2, 4, 6, 8}
C = A & B
print(C)
C = A | B
print(C)
C = A ^ B
print(C)
C = A - B
print(C)
C = B - A
print(C)