# this is a programe to continue to loop and make your programe to jump unconditionaly from loop 

for i in range(0,3):
    a = int(input("enter first number"))
    b = int(input("enter second number "))
    if(b == 0):                                 #here we use conditional operater ==
        print("b can't be zero ")
        continue
    c = a/b
    print(c)
    print(i)