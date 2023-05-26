#Easy 
#Check whether a string is the same forwards and backwards (Palendrome)
string=str(input("Enter a string to check whether it is a palendrome ")).lower()
#Size of 1st half of string
halflen=len(string)//2
#1st half of string
half1=string[0:halflen]
#2nd half of string
half2=string[halflen:]


check=True
for i in range(halflen):
    if half1[i]!=half2[-i-1]: #Checks if each value in the list is the same as the reflected value
        check=False 
if check:
    print("This is a palendrome")
else:
    print("This is not a palendrome")

#-------------------------------------------------------------------------
#Using fancy python:
string=str(input("Enter a string to check whether it is a palendrome "))
if string==string[::-1]:
    print("This is a palendrome")
else:
    print("This is not a palendrome")
#How does this code work: 
#The first colon : indicates the slicing operation.
#The second colon : specifies the step value. 
#In this case, -1 means we are stepping backward through the string. By default, it is 1