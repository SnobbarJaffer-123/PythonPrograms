# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 08:36:29 2022

@author: User
"""

#in optional paramerers , values are set as in parameters .
#if values are passed as arguments (during function call),it will be prioror then values set in parametetrs
def func(x,txt="jaffer"):
    print(x,txt)
    
func('snobbar','jaffer')  
func('snobbar','shameema')
func('snobbar')