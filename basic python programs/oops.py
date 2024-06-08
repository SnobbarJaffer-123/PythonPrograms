# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 09:38:15 2022

@author: User
"""
import turtle
x=5
y='         hello string'
print(type(x))
print(type(y))
print(y.strip())#strip method is used to remove all the leadind and trailing spaces from a string

print(y)

tim=turtle.Turtle()
def func(x):
    return x+1
print(func(5))


#CLASSES AND OBJECTS
class Dog(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def speak(self):
        print('hii,im',self.name,'and i m',self.age,'years old')
        
    def talk(self):
        print('bark')
        
    def change_age(self,age):
        self.age=age
        
    def add_weight(self,weight):
        self.weight=weight
        
tim=Dog("tom",55)
fred=Dog("fred",33)
tim.change_age(5)
tim.add_weight(50)
fred.add_weight(33)
tim.speak()
fred.speak() 

print(tim.weight)
print(fred.weight)


#INHERITANCE
class Cat(Dog):#cat is inherited from dog
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color=color
        self.name='tech'
        
    def talk(self):
        print('meow')

jim=Dog('jim',70)
jim.talk()

tim=Cat('tim',15,"white")
tim.speak()

#inheritance example
class Vehicle():
    def __init__(self,price,gas,color):
        self.price=price
        self.gas=gas
        self.color=color
        
    def fillUpTank(self):
        self.gas=100
    def emptyTank(self):
        self.gas=0
    def gasLeft(self):
        return self.gas

class car(Vehicle):
    def __init__(self, price, gas, color,speed):
        super().__init__(price, gas, color)
        self.speed=speed
        
    def beep(self):
        print('beep beep')    

class truck(Vehicle):
    def __init__(self, price, gas, color,tires):
        super().__init__(price, gas, color)
        self.tires=tires
        
    def beep(self):
        print('honk honk')    
        
a=car(500000,100,'red',80)
#CLASSES AND OBJECTS

    

    
















  














     
    