original="abbbcd"
new="bccddef"
count=0
for i in new:
    if i in original:
        pass
    else:
        count+=1 
        original=original+i #adds it to original to prevent counting it twice
print(count)