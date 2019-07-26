print("This is a progerame of printing the table of any two number that you want ")
print("\t\t let enjoy this programe ")
# thking two number from youser 
num1 = int(input("Enter the first number whose table you want ot see"))
num2 = int(input("Enter the second number whose table you want ot see"))

# now this main loginc of printing table 

print("\t%-3s%10s%10s"%("S.no",str(num1)+" x N",str(num2)+" x N"))

for i in range(1,11):
    print("\t%-3d%10d%10d"%(i,num1*i,num2*i))
# Exit from for loop 
print("\t -----Have A Nice Day------")


# this is the outpute of the file 

# This is a progerame of printing the table of any two number that you want
#                  let enjoy this programe
# Enter the first number whose table you want ot see9
# Enter the second number whose table you want ot see19
#         S.no     9 x N    19 x N
#         1           9        19
#         2          18        38
#         3          27        57
#         4          36        76
#         5          45        95
#         6          54       114
#         7          63       133
#         8          72       152
#         9          81       171
#         10         90       190
#          -----Have A Nice Day------

