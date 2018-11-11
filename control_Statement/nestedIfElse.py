num = int(input("enter any number in range 1 to 20"))
if num >1 and num < 20:
    if num >1 and num <10:
        if num>1 and num<5 :
            print("number is b/w 1 to 5")
        else :
            print("number is b/w 5 to 10 ")
    else:
        print("number is grater than 10 but less than 20 ")
elif(num > 20):
    print("number is grater than 20")
elif num <1 :
    print("number is less than 1 ")
else:
    print("by")
