# n=[1,2,3,4,5,6]
# it = iter(n)
#
# for n in it:
#     print(n)
from operator import add

from PIL.ImageChops import subtract


# w="Python"
# i = iter(w)
# for w in i:
#     print(w)

# t = "python"
# i = iter(t)
# while True:
#     try:
#         print(next(i))
#     except StopIteration:
#         break

# l=["Python","Java","Power BI","SQL","AWS"]
#
# it = iter(l)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# def my_gen():
#     for i in range(1,11):
#         yield i
#
# for n in my_gen():
#     print(n)

# def my_func():
#     n = int(input("Enter a number: "))
#     for i in range(1,n):
#         if i%2==0:
#             yield i
#
# for e in my_func():
#     print(e)

# def my_sqr():
#     n = int(input("Enter a number: "))
#     for i in range(1,n+1):
#         yield i**2
#
# for s in my_sqr():
#     print(s)

# def calculator():
#     def add(a,b):
#         return a+b
#     return add
#
# r = calculator()
# print(r(6,8))

# def discount_cal(discount):
#     def apply_discount(price):
#         return price-(price*discount)
#     return apply_discount
# r2=discount_cal(0.2)
# print(r2(500))

# def calculator():
#     def multiplication(a, b):
#         return a * b
#     return multiplication
#
# r = calculator()
# print(r(11,5))

# def decorator(func):
#     def wapper():
#         print("This is python")
#         func()
#         print("This is decorator")
#     return wapper()
# @decorator
# def hlo():
#     print("This is hlo")

# def deco(func):
#     def wapper():
#         func()
#     return wapper()
# @deco
# def hlo():
#     print("File executed Successfully")



# def Greeting(func):
#     def wapper():
#         func()
#     return wapper()
# @Greeting
# def hlo():
#     print("Welcome to the Python Programming Class")

# def deco(func):
#     def wapper():
#         func()
#     return wapper()
# def hlo():
#     print("Manual calling Decorator")
# d = deco(hlo)

# def stud():
#     '''The Docstring is used to display the commend line in output'''
# print(stud.__doc__)

# class stud():
#     '''The Docstring is used to display the commend line in output'''
#     def docstring(self,name,language):
#         self.name = name
#         self.language = language
#
# print(stud.__doc__)