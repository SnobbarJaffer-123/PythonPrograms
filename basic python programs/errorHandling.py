# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 08:58:44 2022

@author: User
"""

#TRY AND EXCEPT (ERROR HANDLING)
text='snobbar' #input('enter text: ")
try:
    number=int(text)
    print(number)
except:
    print('invalid text')