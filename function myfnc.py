'''
def myfnc(x):
    print("inside myfnc", x)
    x = 10
    print("inside myfnc", x)
x = 20
myfnc(x)
print(x)

'''

def myfnc(x, y = 10, z = 10):
    print("x =", x, "y =", y, "z =", z)
x = 5
y = 6
z = 7
myfnc(x, y, z)
myfnc(x, y)
myfnc(x)