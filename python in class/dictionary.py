myInfo={
    "firstname":"snobbar","middleNme":"jaffer","lastName":"war"

}
print(myInfo)

myInfo["sem"]="2nd"
print(myInfo)
myInfo["sem"]="3rd"
print(myInfo)
myInfo["firstname"]=["sania","snober"]
print(myInfo)
myInfo["lastName"]
print(myInfo.pop("sem"))
print(myInfo)

if "sem" in myInfo:
    print(myInfo["sem"])
else:
    print("not available")

for key in myInfo:
    print(key )
    print(myInfo[key])