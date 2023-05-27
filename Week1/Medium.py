#Give the smallest positive integer made of just 0s and 1s that is divisible by an input, n
#For example, if n is 34, the output should be 111010

#Flips all of the bits from left to right to 0s after flipping that bit to a 1
def flip(result,i):        
    result[i]="0"
    if i < len(result)-1:
        flip(result,i+1)
    return result,i
#Function to increment binary
def increment_binary(binary):
    result = list(binary)  # Convert the binary string to a list of characters
    # Iterate over the bits from right to left
    for i in range(len(result) - 1, -1, -1):
        #1st -1 represents the start, 2nd -1 represents the end, 3rd -1 represents the step
        # If the bit is '0', flip it to '1' and break the loop 
        if result[i] == '0':
            result[i] = '1'
            #If you are flipping the LSB, there is nothing to flip after that because it is the last digit
            if i+1 != len(result):
                result=flip(result,i+1)[0]
            break
    # Convert the list back to a string
    result=''.join(result)
    return result

#-------------------------------------------------------------------------------------------------------------

n=int(input("input an n "))
binum="00000000000000000000000000000000000000000000000000000000000000000000000000000000000001"
while int(binum) % n!=0: #Checks whether this value is divisible
    binum=increment_binary(binum)

#These lines removes the 0s from binum
count=0
for i in range(len(binum)):
    if binum[i-count] == "0":
        binum=binum.replace("0","",1)
        count+=1
    else:
        break

print(binum)

#Same thing using python's unbuilt binary (Which makes this an easy question)
n=int(input("input an n "))
count=1
binum=1
while int(binum) % n!=0:#Checks whether this value is divisible
    count+=1
    binum=int(bin(count)[2:]) #Turns incremented value into binary
print(binum)
