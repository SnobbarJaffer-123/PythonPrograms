# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 12:55:14 2022

@author: User
"""

#FUNCTIONS
def addTwo(n1):
    return n1+2


def subtractTwo(n2):
    return n2-2

def square(n1):
    return n1**2

def printString(string):
    print(string)
    
def acceleration(mass,force):
    a=mass*force
    return a
    

newNnumber=addTwo(7)
print(newNnumber)

newNum=subtractTwo(6)
print(newNum)    
    
num=square(5)
print(num)

printString('hello')
printString('my name is snobbar')
    
print(acceleration(5, 4))


#READ FILE FROM FILE.TXT FILE
file=open('file.txt','r')
f=file.readlines()

print(f) 
#to remove \n  
newList=[]
for line in f:
    newList.append(line.strip())
print(newList)

#WRITING TO A TEXT FILE
file=open('file.txt','w')  
file.write('learning python is easy\n') 
file.write('its fun.....')

file.close() 

#USING .COUNT() AND .FIND()
string='hello snobbar'
print(string.find('l'))
print(string.find('o'))
print(string.find('z'))#will return -1 for the one which is not present

if string.count('b')>0:
    print('good')
else:
    print('not good')   

#local and global variables
var=9
loop =True

def func(x):
    newvar=14
    global loop #this is global ,local variable will be prefranced over this
    loop=19
    print(var) #global varible
    
    print(loop)
    
    if x==5:
        return newvar
    
print(func(2))
print(func(5) )   












