#!/usr/bin/env python3
password = "Python is awesome"
user_attempt = input("Enter password: ")
if user_attempt == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")