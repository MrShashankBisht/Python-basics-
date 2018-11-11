#conditions 
# 1) if 
# 2) if-else
# 3) elif (else-if)

for i in range(0,3):
    a = int(input("enter first number"))
    b = int(input("enter second number "))
    if(b == 0):                                 #here we use conditional operater ==
        print("b can't be zero ")
        continue
    c = a/b
    print(c)
    print(i)
    
