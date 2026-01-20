# class Car():
#     brand="BMW"
#     color="red"
   
# c1= Car() # object created 
# print(c1.brand)
# print(c1.color)
# c2=Car()
# print(c2.brand)
# class Student:
#     name="karan"
#     def __init__(self):
#         print(f"fromn self {self}")
#         print("adding new studnet in database ")
# s1= Student()
# #print(type(s1))
# print(f"s1 memory location{s1}")
# s2=Student()
# #print(type(s2))
# print(f"s2 memory location{s2}")

# class Student:
#     def __init__(self,name,marks):
#         self.name=name #instance variables 
#         self.marks=marks #instance varibale

# s1=Student("Murali",90)
# s2=Student("ramu",85)
# print(s1.name,s2.name)


# class employees:
#     comapny="xyz" #class variabel 
#     def __init__(self):
#         pass

#     def __init__(self,emp_name,emp_id,address,salary,position):
#         self.emp_name = emp_name
#         self.emp_id = emp_id
#         self.address = address
#         self.salary = salary
#         self.position = position
# s1 = employees("Ritz",101,"Salem,India",45000,"Developer") #xyz 
# s2 = employees("Raki",102,"chennai,India",25000,"Tech support")
# s3 = employees("sandy",103,"Hydrabad,India",65000,"cyber security")
# s4 = employees("Asma",104,"Delhi,India",35000,"Data Analyst")
# s5 = employees("shri",105,"kerala,India",15000,"UI Designer")
# employees.comapny="wipro technologies"
# print(s1.emp_name,s1.emp_id,s1.address,s1.salary,s1.position,employees.comapny)#WE CAN CALL CLASS VARIABLES WITH CLASS NAME 
# print(s2.emp_name,s2.emp_id,s2.address,s2.salary,s2.position,s2.comapny) # WE CAN ALSO CALL WITH OBJECT NAME ALSO 


# class Student:
#     college_name="University "
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def welcome(self):#instance method
#         print("welcome students ",self.name)

#     def get_marks(self):#instance method
#         return self.marks
    
# s1=Student("vithika",97)
# s1.welcome() # call the methods with respect to the object.methodname
# #Student.welcome(s1)internally python can call liket his 
# print(s1.get_marks())

#create s student class that takes name, marks of 3 subjects as arguments in constructor
# then create a method to print the average 

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum=0
#         for m in self.marks:
#            # sum=sum+m
#             sum += m
#         print(f"heloo {self.name}, your average score is: {sum/3}")

# s1=Student("Kiran kumar",[99,98,97])
# s1.name="iron man" # name is an attriobute we can manupulate attribute value 
# s1.get_avg()

# static methods
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     @staticmethod
#     def hellow():
#         print("heloo welcome")

#     def get_avg(self):
#         sum=0
#         for m in self.marks:
#            # sum=sum+m
#             sum += m
#         print(f"hi {self.name}, your average score is: {sum/3} {s1.hellow()}")
        
# s1=Student("Kiran kumar",[99,98,97])
# s1.name="iron man" # name is an attriobute we can manupulate attribute value 
# s1.get_avg()

# #class methods :
# class Student:
#     college_name="University "
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     @classmethod
#     def change_cname(cls,new_name):
#         cls.college_name=new_name
#         print(cls.college_name)

#     def welcome(self):#instance method
#         print("welcome students ",self.name)

#     def get_marks(self):#instance method
#         return self.marks
    
# s1=Student("vithika",97)
# s1.welcome() # call the methods with respect to the object.methodname
# #Student.welcome(s1)internally python can call liket his 
# print(s1.get_marks())
# Student.change_cname("bangalore_unver")

# class Employee:
#     company = "TCS"      # class/static variable

#     def __init__(self, name, salary):
#         self.name = name        # instance variable
#         self.salary = salary
#         print("hai")
#     def show(self):             # instance method
#         print(self.name, self.salary, Employee.company)

#     @classmethod
#     def change_company(cls, new):
#         cls.company = new       # class method modifying class variable

#     @staticmethod
#     def is_eligible(salary):
#         return salary > 20000   # static method (utility function)

# e1 = Employee("Murali", 30000) #e1.__init__("Murali", 30000)
# e2 = Employee("Kiran", 15000)#e2.__init__("Murali", 30000)

# calling instance method
# e1.show()
# e2.show()

# calling class method
# Employee.change_company("Infosys")

# after company change
# e1.show()
# e2.show()

# calling static method
# print(Employee.is_eligible(30000))
# print(Employee.is_eligible(15000))
# print(e1)


# __str__()

# class Person:
#     def __init__(self,name):
#         self.name = name
#         # print(f"person(name={self.name}")
#     def __str__(self):
#         return f"person(name={self.name})"
    
# p=Person("murali")
# print(p)
# for readable output
# for debugging 
# for logging
# without __str__() output looks like ugly it going to print memory address 

# class Salary:
#     def __init__(self,amount):
#         self.amount=amount

#     def __add__(self,other): #object + object 2 operator overloading 
#         return self.amount + other.amount
    
# s1=Salary(30000)
# s2=Salary(20000)
# print("final amount",s1 + s2)
#Single inheritence 
# class Car:
#     @staticmethod
#     def start():
#         print("the car is started")
#     @staticmethod
#     def stop():
#         print("car is stopped")
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name=name
# car1=ToyotaCar("fortuner")
# car2=ToyotaCar("prius")
# print(car1.name)
# car1.start()
# car1.stop()

# class Car:   #base class
#     @staticmethod
#     def start():
#         print("the car is started")
#     @staticmethod
#     def stop():
#         print("car is stopped")
# class ToyotaCar(Car): #derived class itself and car 
#     def __init__(self,brand):
#         self.name=brand
      
# class Fortuner(ToyotaCar): # cotains 
#     def __init__(self,type):
#         self.type=type
        
# car1=Fortuner("disel")
# print(car1.type)
# car1.start()
# car1.stop()

#multiople inheritence
# class A:
#     VarA="welcome to class A"
    
            

# class B:
#     varB="welcome to class B"

# class C(A,B):
#     varC="welcome class C"
# C1= C()
# print(C1.varC,C1.varB,C1.VarA)
    
# class Car:
#     def __init__(self,type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("the car is started")
#     @staticmethod
#     def stop():
#         print("car is stopped")
# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name=name
#         super().start() #Car.starte()
              
# car1=ToyotaCar("fortuner","electic")
# print(car1.type)
# duck typing polimorphism
# class Car:
#     def start(self):
#         print("car is starting ...")
# class Laptop:
#     def start(self):
#         print("Laptop is booting........")
# def start_device(device):
#     device.start()

# car=Car()
# lap=Laptop()
# start_device(car)
# start_device(lap)

# method overriding:

# payment gateway:

# class Payment:
#     def pay(self):
#         pass
# class UPI(Payment):
#     def pay(self):
#         print("paid using UPI")
# class Card(Payment):
#     def pay(self):
#         print("paid using credit/Debit card ")
# class NetBanking(Payment):
#     def pay(self):
#         print("paid using Netbanking")
# for method in (UPI() , Card(), NetBanking()):
#     method.pay()
    
# n=NetBanking.pay("netbanking")
# u=UPI.pay("pay")



# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def __get__(self,other):
#         return self.marks > other.marks

# s1=Student("murali",97)
# s2=Student("kiraana",80)
# print(s1.marks > s2.marks) # print(s1 > s2)

#method overloading
# class Test:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a + b)

# ob=Test()
# ob.add(10) #error typeError: Test.add() missing 1 required positional argument: 'b'


#mimic method overloading bu using default arguments

class Test:
    def add(self,a,b=0,c=0):
        print(a + b + c)

t=Test()
# t.add(10)
t.add(10,20,30)
t.add(10,20,30)
        