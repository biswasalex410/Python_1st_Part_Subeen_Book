'''
def add(n1, n2):
    return n1 + n2
n = 10
m = 5
result = add(n, m)
print(result)

number1 = 10
number2 = 10
result = add(number1, number2)
print(result)

n1 = 20
n2 = 10
print(add(n1, n2))

print(add(2.5, 3.5))
'''



def cgpa():
    total1=0
    gtotal=0
    grades={"s":"10","S":"10","a":"9","A":"9","b":"8", "B":"8","c":"7",
            "C":"7","d":"6","D":"6","e":"5","E":"5","f":"4","F":"4"}
    name=input("\n Enter the student name:")
    id=input("\n Enter the student ID:")
    n=int(input("\n Enter the No. of Subjects:"))
    print("\n Enter the grades in (S-E) F-arrear")
    marks=[]
    for entry in range(n):
         sc=input("\n Enter the subject code:")
         ma=input("\n Enter the grades in (S-E):")
         g=float(input("\n Enter the grade points:"))
         if ma in grades:
             m=float(grades[ma])
             ma=ma.upper()
             entry=(sc,g,m,ma)
             marks.append(entry)
             if ma=="F":
                mn="0"
             else:
                mn="1"
    if mn=="0":
         print("\n\tNAME:",name)
         print("\n Subject code Grade")
         for entry in marks:
             sc,g,m,ma=entry
             print("\n\t",sc,"\t\t",ma)
             print("\n\nCGPA=ARREAR")
    else:
         print("\n\tNAME:",name,)
         print("\n Subject code Grade")
         for entry in marks:
             sc,g,m,ma=entry
             print("\n\t",sc,"\t\t",ma)
             total1=total1+m*g
             gtotal=gtotal+g
         cgpa=total1/gtotal
         print("\n\nCGPA=",cgpa)
cgpa()
input("\n Press enter key to exit.")