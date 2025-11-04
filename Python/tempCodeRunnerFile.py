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
        super().__init__(type)   #if u want to call any method of the parent class
        self.name=name
        super().start()

car1=ToyotaCar("prius","elecrtic")
print(car1.name)
print(car1.type) 