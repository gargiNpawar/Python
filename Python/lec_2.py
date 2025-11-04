str1="this is a good day"
print(len(str1))

str2="today is sunday"
len1=len(str2)
print(len1)
print(str1+str2)
print(str1+" "+str2)
print(len(str1+" "+str2))

ch=str1[6]#indexing
print(ch)
print(str1[8])

print(str2[1:5])#last index not included in slicing
print(str1[:4]) #0:4
print(str1[5:]) #5:length of str

str3="apple" #-5 -4 -3 -2 -1 #negative index
print(str3[-3:-1])#-1 not included

str4="this function checks for the end of the str"
print(str4.endswith("str"))
print(str4.capitalize())#capitalize 1st char
print(str4.replace("e","m"))
print(str4.replace("end","start"))
print(str4)#no changes in the original string...makes a new one
print(str4.find("function"))
print(str4.find("that"))#gives -1 
print(str4.count("the"))#checks the occurences of the string

name=input("what is ur name:")
print(len(name)) 
str5="$ i am the $ $ymbol"
print(str5.count("$"))

age=int(input("what is ur age: "))
if(age>=18):
    print("u r eliible candidate")
else:
    print("come back another time")    

light=input("What color light due u see??")
if(light=="red"): 
    print("wait as u see",light,"light") 
elif(light=="yellow"):
    print("u watch")      
elif(light=="green"):
    print("go go go")   
else:
    print("error in light")     

num=5
if(num>2):
    print("correct 1") #checks all if condtion statement
if(num>4):
    print("correct 2")    

num2=6
if(num2>=5):
    print("true for con1")    
elif(num2==6):
    print("true for con2") #elif checked only when if is false

num2=6
if(num2<=5):
    print("true for con1")    
elif(num2==6):
    print("true for con2") #elif only printed when if false and elif true

num2=6
if(num2<=5):
    print("true for con1")    
elif(num2==3):
    print("true for con2")
else:
    print("all false")       

marks=int(input("what are ur marks:"))  
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90 ):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"    
elif(marks<70):
    grade="D"
else:
    grade="F" 
print("Grade of the student is:",grade)        

number=int(input("Enter a number in the space_"))
if(number%2==0):
    print(number,"is even")
else:
    print(number,"is odd")    

a=int(input("User pls enter first number"))
b=int(input("User pls enter second number"))
c=int(input("User pls enter third number"))
if((a>=b)and(a>=c)):
    print("a is greatest")
    if(a==b):
        print("a and b are equal")
    if(a==c):
        print("a and c are equal")    
elif((b>=c)):
    print("b is the greatest")
    if(b==c):
        print("b and c are equal")   
else:
    print("c is the greatest")  


num=int(input("Enter a number="))
if(num%7==0):
    print("number is multiple")
else:
    print("Not a multiple")    