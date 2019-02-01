count = 1
s = input("Enter the string to check for palindrome ")
for i in range(0,int(len(s)/2)):
    if s[i] != s[len(s)-i-1]:
        count = 0
if(count == 1):
    print("your string is palindrome")
else:
    print("your string is not palindroms")

