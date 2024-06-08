# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:19:25 2024

@author: User
"""

# greatest among the three numbers
num1=10
num2=5
num3=6
if(num1>=num2) and (num1>=num3):
    largest=num1
elif(num2>=num1) and(num2>=num3):
    largest=num2
else:
    largest=num3
    
    print("greatest among the three is",largest)