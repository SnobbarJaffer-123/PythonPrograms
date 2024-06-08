import math
list=["faisal",'A',123]
print(list)
for i in list:
    print(i)

x=4
list2=[x,x**2+1,math.sqrt(x)]    
for i in list2:
    print(i)

list3=range(1,11)
for i in list3:
    print(i)
myInfo="my name is snobbar"    
list4=myInfo.split()
for i in list4:
    print(i)
list5=["hello"]
#for i in list
print(list5)

"""sentence2=("my name is khan")
print(sentence2)"""
list6=["abc","j",7]
print(list6[0:2])
print(list6[2:3])

if "abc" in list6:
    print("element found")
else: 
    print("element not found")

list7=["nardis","sadath",16,15,32,"snobbar"]
list8=[]
"""for i in list7:
    if type(i)==int:
        list8.append(i)
print(list8) """
listt=[1,2,3,4,5,5,0]
list9=[i for i in list7 if type(i) ==int]
print(list9)

