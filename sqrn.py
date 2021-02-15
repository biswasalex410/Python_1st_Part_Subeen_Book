'''
while True:
    n = input("Please enter a number(0 to exit): ")
    n = int(n)
    if n == 0:
        break
    print("Square of", n, "is", n*n)
'''

while True:
    n = input("Please enter a positive number (0 to exit):")
    n = int(n)
    if n < 0:
        print("We only allow positive number. please try again.")
        continue
    if n == 0:
        break
    print("Sqare of", n, "is", n*n)