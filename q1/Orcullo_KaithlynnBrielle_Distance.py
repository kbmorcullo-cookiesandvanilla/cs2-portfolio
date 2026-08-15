import math

x1 = int(input("Give me x1 coordinates: "))
y1 = int(input("Give me y1 coordinates: "))
x2 = int(input("Give me x2 coordinates: "))
y2 = int(input("Give me y2 coordinates: "))

son = (math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
boi = math.sqrt(son)

print("The difference is,", boi)

#Reflection
#The math library let me get the square root and put them in  the power of 2 easier and faster.
#If these functions weren't available I'd propably look for a way to do it by finding a step-by-step way to do it.
