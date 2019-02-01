# pallindrome numbers 
# n=int(input("Enter number:"))
# temp=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
# if(temp==rev):
#     print("The number is a palindrome!")
# else:
#     print("The number isn't a palindrome!")

# now palindrome String
count = 1
s = input("Enter the string to check for palindrome ")
for i in range(0,len(s)/2):
    if s[i] != s[len(str)-i-1]:
        count = 0
if(count == 1):
    print("your string is palindrome")
else:
    print("your string is not palindroms")