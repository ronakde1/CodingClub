#Easy 
#Check whether a string is the same forwards and backwards (Palendrome)
string=str(input("Enter a string to check whether it is a palendrome "))
#Size of 1st half of string
halflen=int(len(string)/2)
#1st half of string
half1=string[0:halflen]
#2nd half of string
half2=string[halflen:-1]
print(half1)
print(half2)