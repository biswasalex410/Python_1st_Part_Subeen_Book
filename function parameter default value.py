def myfnc(x, z, y = 10):
    print("x= ", x, "y=", y, "z= ", z)
myfnc(x = 1, y = 2, z = 5)
a = 5
b = 6
myfnc(x = a, z = b )
a = 1
b = 2
c = 3
myfnc(y = a, z = b, x = c)