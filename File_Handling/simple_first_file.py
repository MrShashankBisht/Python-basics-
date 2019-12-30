# this is a simple file handling programe

print("Here you can create and Read file ")
print('\n\t 1. For Create file \n\t 2. For write in file \n\t 3. For Read from File ')
option = int(input("Enter your option ==> "))
if option == 1:
    fname = input("enter the file name here -> ")
    file = open(fname,'w')
  

elif option ==2 :
    fname = input("enter the file name here -> ")
    file = open(fname,'a')
    strs1 = input("enter any msg")
    file.write("\n"+strs1)

elif option ==3 :
    fname = input("enter the file name here -> ")
    file = open(fname,'r')
    str1 = file.read()
    print(str1)
    

else :
    print("plz enter the corrected option ")

file.close()