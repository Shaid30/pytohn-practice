class Student:
    def __init__(self,name,marks): #constructor method
        self.name = name
        self.marks = marks
        print("new database")

s1 = Student("arjun",89)
print(s1.name,s1.marks)


#practice Qs
class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
    def debit(self,amount):
        self.balance -= amount
        print("Tk",amount,"was debited")
        print("total_balance=",self.get_balance())
    def credit(self,amount):
        self.balance +=amount
        print("Tk",amount,"was credited")
        print("total_balance =", self.get_balance())
    def get_balance(self):
        return self.balance
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(2000)




#single inheritance
class Car:
    def __init__(self,type):
        self.type = type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
class Toyotocar(Car):
    def __init__(self,name):
        super().__init__(type) #using super method
        self.name = name
        super().start() #super method

car1 = Toyotocar("fortuner")
car2 = Toyotocar("MERCEDEZ")
print(car1.stop())


#multiple inheritance
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"
class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)



        

