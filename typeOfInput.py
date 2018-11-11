name = input("enter your name : ")
age = int(input("enter your age : "))
marks = float(input("enter your marks : "))

print(type(name))
print(type(age))
print(type(marks))

nameList = []
for name in range(1,10):
    name = input('Enter the name for the list')
    nameList.append(name)

print(nameList)