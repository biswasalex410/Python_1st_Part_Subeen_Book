
'''
year = input("Enter the year:")
year = int(year)

if year % 4 != 0:
    print("NO !!!!!! It is not Leap Year")

else:
    if year % 100 == 0:
        if year % 100 == 0:
            print("YES!!! It is Leap Year")
        else:
            print("NO !!! It is not Leap Year")
    else:
        print("YES !!!!!!  It is Leap Year")

'''


'''
year = input("Enter the year:")
year = int(year)

if year % 400 == 0:
    print("Yes")
elif year % 100 == 0:
    print("No")
elif year % 4 == 0:
    print("Yes")
else:
    print("No")
'''


year = input("Enter the year:")
year = int(year)

if year % 100 != 0 and year % 4 == 0:
    print("Yes !!!  It is leap year")

elif year % 100 == 0 and year % 400 == 0:
    print("Yes !!! It is leap year")
else:
    print("No !!! It is not leap year")
