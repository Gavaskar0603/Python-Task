# from pyexpat import model
#
#
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#
# class Brand(Mobile):
#     def display(self):
#         print("Brand Name:",self.brand)
#
# class Model(Mobile):
#     def display(self):
#         print("Model Name:",self.model)
#
# class Price(Mobile):
#     def display(self):
#         print("Price:",self.price)
#
# m1=Mobile("Realme","RealmeC3",18000)
#
# # b=Brand()
# # m=Model()
# # p=Price()
#
# m1.brand()
# m1.model()
# m1.price()


# class Employee:
#     def __init__(self,emp_id, name, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.salary = salary
#
# class emp_id(Employee):
#     def func(self):
#         print(self.emp_id)
#
# class name(Employee):
#     def func(self):
#         print(self.name)
#
# class salary(Employee):
#     def func(self):
#         print(self.salary)
#
# e=Employee(12,"Python",14000)
# e2=Employee(13,"Java",18000)
#
# print("Employee ID:",e.emp_id)
# print("Employee Name:",e.name)
# print("Salary:",e.salary)
# print("Employee ID:",e2.emp_id)
# print("Employee Name:",e2.name)
# print("Salary:",e2.salary)

# class Rectangle(ABC):
#     @abstractmethod
#     def calculation(self, width, height):
#         pass
#
# class rect_area(Rectangle):
#     def calculation(self,width,height):
#         return width*height
# class rect_perimeter(Rectangle):
#     def calculation(self,width,height):
#         return 2*(width+height)
#
# a = rect_area()
# b = rect_perimeter()
#
# res = a.calculation(2,3)
# res2 = b.calculation(2,3)
# print("Area",res)
# print("Perimeter",res2)

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display_person(self):
#         print("Person Name:",self.name)
#         print("Age:",self.age)
#
# class teacher(person):
#     def __init__(self, name, age, subject, salary):
#         super().__init__(name, age)
#         self.subject = subject
#         self.salary = salary
#
#     def display_teacher(self):
#         self.display_person()
#         print("subject:",self.subject)
#         print("salary:",self.salary)
#
# t=teacher("Ram",23,"Python",18000)
#
# t.display_teacher()

# class Vehicle:
#     def speed(self):
#         print("Vehicle speed")
#
# class Bike(Vehicle):
#     def speed(self):
#         print("Bike speed 100 km/h")
#
# v = Vehicle()
# b = Bike()
#
# print("Vehicle:")
# v.speed()
# print("Bike:")
# b.speed()


# class Account:
#     def __init__(self):
#         self.__balance = 0
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: {amount}")
#         else:
#             print("Invalid deposit amount")
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdraw: {amount}")
#         else:
#             print("Insufficient balance or invalid amount")
#
#     def show_balance(self):
#         print(f"Current balance: {self.__balance}")
#
# a = Account()
#
# a.deposit(1000)
# a.withdraw(500)
# a.show_balance()

# class Dog:
#     def sound(self):
#         print("Dog: Barks")
#
# class Cat:
#     def sound(self):
#         print("Cat: Meows")
#
# class Cow:
#     def sound(self):
#         print("Cow: Moos")
#
# animals = [Dog(), Cat(), Cow()]
#
# for animal in animals:
#     animal.sound()


# from abc import abstractmethod, ABC
# import math
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
# c = Circle(5)
# r = Rectangle(4, 6)
#
# # Calculate areas
# print(f"Circle area: {c.area()}")
# print(f"Rectangle area: {r.area()}")

# class Customer:
#     def __init__(self, name, account_number):
#         self.name = name
#         self.account_number = account_number
#         self.balance = 0
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print(f"Withdraw: {amount}")
#
#     def check_balance(self):
#         print(f"Current balance: {self.balance}")
#
#
# class Bank:
#     def __init__(self):
#         self.customers = {}
#
#     def create_account(self, name, account_number):
#         if account_number in self.customers:
#             print("Account already exists")
#         else:
#             self.customers[account_number] = Customer(name, account_number)
#             print("Account created successfully")
#
#     def get_customer(self, account_number):
#         return self.customers.get(account_number)
#
#
# def main():
#     bank = Bank()
#     while True:
#         print("\nBank Management System")
#         print("1. Create account")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Check balance")
#         print("5. Exit")
#         choice = int(input("Enter your choice: "))
#
#         if choice == 1:
#             name = input("Enter name: ")
#             account_number = input("Enter account number: ")
#             bank.create_account(name, account_number)
#         elif choice == 2:
#             account_number = input("Enter account number: ")
#             customer = bank.get_customer(account_number)
#             if customer:
#                 amount = float(input("Enter amount to deposit: "))
#                 customer.deposit(amount)
#             else:
#                 print("Account not found")
#         elif choice == 3:
#             account_number = input("Enter account number: ")
#             customer = bank.get_customer(account_number)
#             if customer:
#                 amount = float(input("Enter amount to withdraw: "))
#                 customer.withdraw(amount)
#             else:
#                 print("Account not found")
#         elif choice == 4:
#             account_number = input("Enter account number: ")
#             customer = bank.get_customer(account_number)
#             if customer:
#                 customer.check_balance()
#             else:
#                 print("Account not found")
#         elif choice == 5:
#             break
#         else:
#             print("Invalid choice")
#
# main()
