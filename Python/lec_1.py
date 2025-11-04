print("hello world") #case sensitive
print("iam gargi pawar","i study at mit")
print(89)
print(89+77)

name="gargi" #string
age=21 #int
price=23.9 #float
age2=age
print("my name is:",name)
print("my age is:",age)
print("my age is",age2)

print(type(name))
print(type(age))
print(type(price))

name1="ramu"
name2='ramu'
print(name1)
print(name2)

old=False #boolean
a=None #none
print(type(old))
print(type(a))

a=2
b=5
sum=a+b
print(sum)

"""
arithmetic operators + - * / % **
relational operators == != >= > <= <
assignment operators = += -= *= /= %= **=
logical operators not  not true/false  and or 

"""
num=10
num+=10 #num=num+10
print(num)

a=50
b=20
print(not False)
print(not (a>b))
print('and operator:',(a==b) and (a>=b) ) #f t=f
print('or operator:',(a==b) or (a>=b) )  #f t=t

a=2
b=3.14
sum=a+b
print(sum)

c=float("3")#typecast
d=5.03
sum2=c+d
print(sum2)

#input
name=input("Your name please: ")
print("welcome to the RR restraunt",name)

age=input("enter ur age")
print(type(age),age)

age=int(input("enter ur age"))
print(type(age),age)

name=input("sir please enter ur name=")
age=int(input("ur age pls="))
marks=float(input("enter ur marks="))
print("welcome",name)
print("age is:",age)
print("marks=",marks)

a=int(input("a:"))
b=int(input("b:"))
sum=a+b
print("sum of nos is=",sum)

side=int(input("Enter the side of the sqaure="))
print("area of square is:",side * side)

side=float(input("Enter the side of the sqaure="))
print("area of square is:",side ** 2)

c=float(input("first :"))
d=float(input("second :"))
print("avg",(c+d)/2)

a=int(input("a:"))
b=int(input("b:"))
print("a>=b is:",a>=b)
