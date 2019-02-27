print("First things first ... Love myself!")

MyList = ["Banana","Apple","Microsoft","Lamborgini"]

for items in MyList:
    print(items)

MyList.append("Rubber Ducky")
print (MyList)
MyList.pop(MyList.index("Microsoft"))

MyList.append("Orange")

print (MyList)