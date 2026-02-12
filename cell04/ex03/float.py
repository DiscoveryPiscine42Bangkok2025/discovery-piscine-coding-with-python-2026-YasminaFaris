#!/usr/bin/env python3

num = input("Give me a number: ")

num_float = float(num)

if num_float.is_integer() :
    print("This number is an integer.")
else :
    print("This number is a decimal.")