#Every thing about string

    #1) concatenate
    #2) upper and lower case string convert
    #3) title

str1 = "hello novice programmer"
str2 = "HI WHATS GOING ON PYTHON"
print(str1.upper())             # e.g -> A,B,C,.,.,.
print(str2.lower())         
num = 3
intStr = str(num)               #conversion of a int type variable into string type variable 
print(str2.lower() + intStr)
print(str1.title())
# address of the string objects in python
#num = int(input("enter any number"))
#str = str(num)
#str2 = '45'
#print(type(str))
#print(type(str2))
#print("Addrss of str ==>",id(str))
#print("Address of str2 ==> ", id(str2))

string1 = "welcome"
string2 = "welcome"
print('\n ',id(string1),'\n ',id(string2))


# concatenation of the 

print(string1 + string2)
