# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print(3+6)
num=55
print(num)

    
"""
import matplotlib.pyplot as plt  
  
x=[1,2,3,4,5,6]
y=[6,5,4,3,2,1]

plt.plot(x,y)
plt.barh(x,y)
plt.show()
"""
"""
print('pick a number')
num1 = input()
print('pick another number')
num2 = input()
add=int(num1)+int(num2)
print (add)
"""
#conditionals
print(4<5)
print('hello'!='hii')

#decisions
age=input('input ur age')
#age=17
if int(age)<16:
    print('hay u cannot ride,under 16')
elif int(age)>16:
    print("u can ride,over 16")
else:
    print('u can start ur ride for now')
    
#chain conditionals and nested statements
x=3
y=2
if x==y and x+y==5:
     print('run')
else:
    print(':(') 
    
if y==x or x+y==5:
    print('snobbar')
    
if not(y==x or x+y==6 ):
    print('hii') 
    
#nested conditions
if x==3:
    if y==2:
        print('x=3 and y==2')
    else:
        print('')
        
else:
    print('x!=3') 
    
#for loop
for i in range(1,10,2): #start,stop and step
    print(i )
"""
#while loops
loop=True

while loop:
    name =input('insert something')
    if name =='snobbar':
        break
  """  
    
#lists and tuples
fruits=['apple','pear','mango','bananas',4]
print(fruits)
print(fruits[2])
fruits.append('strawberry')
print(fruits)
fruits[4]='blueberry'
print(fruits)
  
#tuples are used for coordinance and colors and rectiangulars n many more
positions=(2,3)
color=(255,255,255)
print(type(color)) 

#iteration by item 
for fruit in fruits:
    print(fruit)
    
#
for fruit in fruits:
    if fruit=='pear':
        print(fruit) 
    else:
        print('not pear')
    
#STRING METHODS
# .strip(), len(), .lower(), upper(), .split()  

#.strip method removes all the leading and trailing white spaces from a string
text="   hello   "#input ('input something')
print(text.strip())

#length of text using function    
print(len(text))

#turning everything into lower case   

text2="ASALAMUALAIKUM"
print(text2.lower())

#turns everything inti upper case 
print(text.upper()) 

#split function splits the strings by any delemeter we give that we put inside of parenthesis of split function

text3="hii.my.name .is. snobbar"
print(text3.split('.'))

print(text.split("l"))
    
#SLICE OPERATOR
s="CUT THE SLICE OF string "
print(s[4:])  #strat fron the index till the last
print(s[::2])   #from 0 to last index but step by 2
print(s[3::3])

fruits[2:2]='p'  #appends papaya at position 2
print(fruits)

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



    
    
    
    
    
    
    
    
    
    
    
    