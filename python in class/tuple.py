tuple1=("snobbar","nargis","sadath")
for i in tuple1:
    if i=="snobbar":
        print(i)
"""tuple1.pop()   
print(tuple1)

tuple1.append("qurat") """     
print(tuple1)
"""del().tuple1    
print(tuple1)"""
mylist=list(tuple1)
mylist.append("Qurat")
print(mylist)
myTuple=tuple(mylist)
print(myTuple)

for i in myTuple:
    if i=="sadath":
        print(i)

if "nargis" in myTuple:
    print("hii nargis")
else:
    print("sjhkjk")

"""nested tuple"""
tuple2=("nargis","sadath",("snobbar","jaffer"),["qurat","bintul"],"sadath")    
print(tuple2)
print(tuple2[2])
print(tuple2[3][0])
print(tuple2[3][0][0])
print(tuple2[-1])
print(tuple2.count("sadath"))
print(tuple2.index("sadath"))