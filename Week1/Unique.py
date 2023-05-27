import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
#This creates a figure and returns the fig and ax.
#Fig is a variable assigned to the figure object. This is  not important when plotting 1 graph.
#ax is the axes object which represents a set of axes within the figure. Below, this is used to define the limits of the size of the graph.

plt.plot(0.5,0.5,".",color="yellow",markersize=500) #Makes the outside yellow
#Creates the eyes
plt.plot(0.65,0.6,".",color="black",markersize=25) 
plt.plot(0.35,0.6,".",color="black",markersize=25)

#Draws the simley face
x = np.linspace(0.3, 0.7, 100) #Creates 100 evenly spaced values of x between 0.3 to 0.7
y =  3*(x - 0.5) ** 2 +0.2 #Quadratic that creates the simley face
plt.plot(x, y,color="black") #Plots this

#sets the size of the plot from 0,0 to 1,1
ax.set_xlim(0, 1) 
ax.set_ylim(0, 1)
ax.axis('off')

plt.show()
