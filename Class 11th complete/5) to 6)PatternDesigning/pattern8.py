n = int(input("enter the number of row in your simple pattern = "))
print("\n")
temp = n
for i in range(n):
    for j in range(0,temp):
        print(end=" ")
    temp -= 1
    for k in range(0,i+1):
        print("*", end=" ")
    print("\n")
for i in range(n,0,-1):
    for j in range(0,n-i+1):
        print(end=" ")
    for k in range(0,i):
        print("*", end=" ")
    print("\n")


# ---------------------------output of the above code is given bellow ------------------------


# enter the number of row in your simple pattern = 6

#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
#  * * * * * *
#  * * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *