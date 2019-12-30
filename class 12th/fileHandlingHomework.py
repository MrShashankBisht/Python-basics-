# This is a file handling programme where we can create 
# file and insert data of employe (employe number, employee name and employee salary) 
# and read salary from the file 
print("This is a File Handling Programer");
print("We have Following Option to Perform diff Operation to file \n 1) Create File \n 2) Insert data To file \n 3) Delete Data from File \n 4) Read data from file \n 5) delete file \n 6) Increse Salary Of Employe \n 7) Exit")
opt = int(input("Enter the Currect Option"))
name = input("\n enter the file name with extension ");
if(opt==1):
    file = open(name,"w")
elif opt == 2:
    num = 1
    file2 = open(name,"r")
    file2.flush()
    for count in file2.readline:
        num = num + 1
    print(num)
    file = open(name,"a+")
    e_name = input("Enter the Name of Employe")
    e_salary = int(input("Enter Salary of "+e_name))
    file.write("%-3d%20s%20d"%(num,e_name,e_salary)+"\n")

