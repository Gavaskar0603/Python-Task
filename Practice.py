import time
# def greet():
#     print("Hello World")
#     time.sleep(5)
#     print("Welcome to Python Threads")
#
# greet()

import threading
from http.client import responses

# def task1():
#     for i in range(3):
#         print("Task 1 is running")
#         time.sleep(5)
# def task2():
#     for i in range(3):
#         print("Task 2 is running")
#         time.sleep(5)
# t1 = threading.Thread(target=task1)
# t2 = threading.Thread(target=task2)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
# print("Both Task 1 and Task 2 are done")

# def background():
#     for i in range(5):
#         print("Background Task is running",i)
#         time.sleep(1)
# t = threading.Thread(target=background)
# print("Background Task is Finished!\n")
# t.start()

# import requests
# response = requests.get("https://www.github.com")
# print("Response Code:",response.status_code)
# print("Response text:",response.text)

# import socket
# website = "www.google.com"
# ip = socket.gethostbyname(website)
# print(f"The IP address of {website} is {ip}")

import pymysql
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE project")


# create database project;
# use project;
# create table sample(id int,name varchar(30),Course varchar(25));
# insert into sample values(1,"Adhi","AI Developer"),(2,"Ajay","Data Science");