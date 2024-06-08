# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 07:27:07 2022

@author: User
"""

#INTRODUCTION TO MODULAR PROGRAMMING
#python modules and import statements
#python is modular programming language means we can use multiple files together to create one program
#e.g we have inbuild 'math','os','pygame' modules  we can also create our own module
import math  #inbuild module
import os
import myModule  #we can create our own module
import pygame #for game development
print(math.pi)
print(math.sqrt(25))

print(myModule.myFunc(5))
print(myModule.anotherFunc(34543))