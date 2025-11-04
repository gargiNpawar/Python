"""
procedural
    |
functional
    |
object oriented programming

"""
class Car:  #class
    color="blue"          #common for all cars
    brand="mercedes"
    No_of_seats="two seater"
car_1=Car()  #object
print(car_1.No_of_seats)
print(car_1.brand)


class Student:
    def __init__(self): #THIS IS A CONSTRUCTOR AND SELF IS 1ST PARAMETER
        print(self)
             #self and s1(current instance/object are the same thing)
s1=Student()
print(s1)

class Student:
    def __init__(self, fullname):  #fullname is the attribute/next parameter
        self.name = fullname    #name variable created in the class
        print("adding new students")

s1 = Student("karan")
print(s1.name)

#karan is passed into fullname and in self ie s1 student ,name variable is created that gets assigned fullname value

class Student:
    #PARAMETERISED CONSTRUCTOR
    college="MIT ADT UNIVERSITY"  #class attribute
    def __init__(self,name,marks):  #name and marks are attributes/parameters
        self.name = name    #object attribute >> class attribute
        self.marks=marks
        print("adding new students")
    
    @staticmethod     #it works at class level...no use of obj attribute
    def welcome(self):      #decorator
        print("Wlc to the class",self.name)   

    def get_marks(self):    #methos or functions
        return self.marks     

s1 = Student("karan",84)
print(s1.name,s1.marks)
s1.welcome()

s2=Student("rahul",77)
print(s2.name,s2.marks)
print("U got :",s1.get_marks(),"marks")

print(s2.college)
print(Student.college)


class Student:
    #DEFAULT CONSTRUCTOR
    def __init__(self): #NOTHING OTHER THAN SELF
        pass


class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("HELLO",self.name,"your avg marks are:",sum/3)    


s1=Student("dr geller",[34,56,89])        
s1.get_avg()

#abstraction=hiding the implementation details of a class...only show essential features
#encapsulation=wrapping the data and functions into a single unit

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.acc=True
        self.clutch=True
        print("car started")

car1=Car()
car1.start()  #abstraction where u dont see the inner details of car start

class Account:
    def __init__(self,bal,acc_no):
        self.balance=bal
        self.account_no=acc_no

    def debit(self,amount):
        self.balance-=amount
        print("RS",amount,"was debited")
        print("Total balance:",self.get_balance())

    def credit(self,amount):
        self.balance+=amount
        print("RS",amount,"was credited")
        print("Total balance:",self.get_balance())

    def get_balance(self):
        return self.balance

acc1=Account(10000,215)  
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(4000)
