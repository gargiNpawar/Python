class Student:
    def __init__(self,name):
        self.name=name

s1=Student("shraddha")
del s1
print(s1)


class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass #__acc_pass becomes a private attribute
    
    def reset_pass(self):     #passed into internal class method
        print(self.__acc_pass)

acc1=Account("1234","abced")
print(acc1.acc_no)
print(acc1.__acc_pass)    #It cannot be accessed outside the class
acc1.reset_pass()


class Person:
    __name="annoymous"

    def __hello(self):
        print("hello eneryone")

    def welcome(self):
        self.__hello()   #interal call method calling __hello function 

p1=Person()
print(p1.__hello()) #shows error
print(p1.welcome())



class Car:   #PARENT CLASS 1
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")    

class ToyotaCar(Car):    #OBJECT CLASS 1
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Fortuner")
car2=ToyotaCar("eclipse")

print(car1.name)
car1.start()    #SINGLE LEVEL INHERITANCE


class Car:  #PARENT CLASS 1
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")    

class ToyotaCar(Car):           #OBJECT CLASS 1----type of car
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):    #OBJECT CLASS 2----brand of toyota car
    def __init__(self, fuel_type):
        self.fuel_type=fuel_type
        
car1=Fortuner("diesel")
car1.start()            #MULTI-LEVEL INHERITANCE

 
class A:    #PARENT CLASS 1
    varA="welcome to class A"

class B:    #PARENT CLASS 2
    varB="welcome to class B"

class C(A,B):   #CHILD CLASS...INHERITS FROM TWO BASE CLASS
    varC="welcome to class C"

c1=C()
print(c1.varC)
print(c1.varB)   #MULTIPLE INHERITANCE
print(c1.varA)


#SUPER KEYWORD
class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")    

class ToyotaCar(Car):           
    def __init__(self,name,type):
        super().__init__(type)   #if u want to call any def of the parent class we use SUPER keyword
        self.name=name
        super().start()

car1=ToyotaCar("prius","elecrtic")
print(car1.name)
print(car1.type) 

