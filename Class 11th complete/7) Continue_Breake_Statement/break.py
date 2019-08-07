# this is a programe to break your loop and make your programe to jump unconditionaly from loop 
# in this programe we take inpute from user and quit loop(uncondionaly break the middle term )
num = int(input('Enter the Ending limit of the loop '))
for i in range (num):
    print("you are in loop and this is looping number := ",i)
    if(i % 3 == 0):
        break
    print('at the end of the loop')
    