'''

# cheking module & package

import builtins
print(dir(builtins))
'''

'''
# amra standard library import kore ksu package er function or module use kore dekhi

import math
print(math.pi)
print(math.pow(2, 3))
print(math.sqrt(25))
print(math.floor(5.2))
print(math.ceil(5.2))
'''

'''
# amra ajker date jante chai

import datetime
today = datetime.date.today()
print(today)

# abar jodi bortoman time shoho jante cai

import datetime
today = datetime.datetime.today()
print(today)

'''

'''

# module theke sudhu class import kore o kaj kora  jay

from datetime import datetime
d = datetime.today()
print(d)

'''

'''
# amra website o visit korte pari web browding er maddhome

import webbrowser
url = "http://google.com"
webbrowser.open(url)


# shortcut a code kore o amra web browser open korte pari

import webbrowser as wb
url = "http://google.com"
wb.open(url)

'''

'''

# new module toiri kora

def find_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
         i += 1
         fib_x, fib_next = fib_next, fib_x + fib_next
    return fib_next


for x in range(1, 11):
    print(find_fib(x))
    
'''



def find_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1

    i = 3
    while i <= n:
         i += 1
         fib_x, fib_next = fib_next, fib_x + fib_next
    return fib_next


for x in range(1, 11):
    print(find_fib(x))
