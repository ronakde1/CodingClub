#part 3
speedx=float(input("Enter speed x "))
speedy=float(input("Enter speed y "))
time=float(input("Enter time "))

distancex=round(speedx*time,10)
distancey=round(speedy*time-9.8*(time**2)/2,10)
print(f"Coordinates after time {time} is {distancex},{distancey}")

#part 2
accelerationx=float(input("Enter acceleration x"))
accelerationy=float(input("Enter acceleration y"))
time=float(input("Enter time "))

distancex=round(speedx*time+accelerationx*(time**2)/2,10)
distancey=round(speedy*time+accelerationy*(time**2)/2,10)
print(f"Coordinates after time {time} is {distancex},{distancey}")

#part 3 
changeaccelerationx=float(input("Enter change in acceleration x"))
changeaccelerationy=float(input("Enter change in acceleration y"))
time=float(input("Enter time "))

distancex=round(speedx*time+accelerationx*(time**2)/2+changeaccelerationx*(time**3)/6,10)
distancey=round(speedx*time+accelerationy*(time**2)/2+changeaccelerationy*(time**3)/6,10)
print(f"Coordinates after time {time} is {distancex},{distancey}")