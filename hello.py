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




class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem 
        self.math = math

    @property         #property method
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"

stu1 =Student(98,65,64)
print(stu1.percentage)

stu1.phy=78
print(stu1.percentage)

#polymorphism and dunder function
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def showNumber(self):
        print(self.real,"i +",self.img, "j")
    def __add__(self, num2):
        newReal =self.real+num2.real
        newImg = self.img +num2.img
        return Complex(newReal, newImg)
num1 =Complex(1,3)
num1.showNumber()

num2 =Complex(4,6)
num2.showNumber()

#practice QS 
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 *self.radius**2
    def perimeter(self):
        return 2 * 3.14 * self.radius
c1 =Circle(22)
print (c1.area())
print (c1.perimeter())


#QS 2
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def showDetails(self):
        print("role=", self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super ().__init__("Engineer", "IT","60,000")

engg1 = Engineer("Elon Musk", "40")
engg1.showDetails()

#QS 3
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,odr2): #using dunder function
        return self.price > odr2.price


odr1 = Order("chips","20")
odr2 = Order("tea", "15")
print(odr1>odr2)

#Guess the number concept
import random

target = random.randint(1, 100)
while True:
    UserChoice = input("Guess the target or Quit: ")
    if(UserChoice == "Quit"):
        break
    UserChoice = int(UserChoice)
    if(UserChoice== target):
        print("Sucess:Correct Guess!!")
        break
    elif(UserChoice<target):
        print("your number is too small. take a bigger guess")
    else:
        print("your number is too big. take a smaller guess")

print("........GAME OVER.......") 

#RANDOM PASSWORD GENERATOR
import random
import string

pass_len =12
charValues = string.ascii_letters+ string.digits+string.punctuation

password = " "
for i in range(pass_len):
    password +=random.choice(charValues)

print ("your random passwor is :", password)

#number pattern
for i in range(6):
    for j in range(1,i+1):
        print(j,end="")
        print("")