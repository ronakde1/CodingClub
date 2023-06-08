import matplotlib.pyplot as plt
i=0
x=0
y=0
matrix=[]
pythagoras=[]
for e in range(50):   
    matrix.append([x,y])
    while y>0:
        x+=1
        y-=1
        matrix.append([x,y])
        i+=1
        if x>y and y!=0 and x!=0:
            tempx=x**2-y**2
            tempy=2*x*y
            #tempz=x**2+y**2
            pythagoras.append([tempx,tempy])

    x+=1
    matrix.append([x,y])
    while x>y:
        x-=1
        y+=1
        matrix.append([x,y])
        if x>y:
            tempx=x**2-y**2
            tempy=2*x*y
            #tempz=x**2+y**2
            pythagoras.append([tempx,tempy])
    y+=1

print(pythagoras)

#for a,b in matrix:
    #plt.plot(a,b,".",color="black",markersize=5)
for a,b in pythagoras:
        plt.plot(a,b,".",color="blue",markersize=5)
plt.show()