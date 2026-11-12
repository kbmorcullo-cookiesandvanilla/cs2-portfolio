#Exercise 1: Count Even Numbers
#Using a for loop, display all even numbers from 2 to 20.
#Hint: Use range() with a step of 2

for a in range(2,22,2):
  print(a)

#I made it print the code.
----------------------------------------------------------------------------------------------------------------------
#Exercise 2: The Countdown Timer
#Create a program that displays numbers from 10 down to 1. After the countdown, display "Time is up!" 
#Hint: Use a while loop

countdown = 10
while countdown >= 1:
  print(countdown)
  countdown -= 1
  if countdown == 0:
    print("Time is up!")
    break

#I made it subtract one each time and when it was equal to 0 I made it print "Time is up!".
----------------------------------------------------------------------------------------------------------------------
#Exercise 3: Skip Multiples
#Display numbers from 1 to 15, but skip every multiple of 3.
#Hint: Use the modulo (%) operator and continue
a = 1
for a in range(1,15):
  if a == 3:
   continue
  elif a == 6:
    continue
  elif a == 9:
    continue
  elif a == 12:
    continue
  print(a)
  #I just made the code "continue" for each multiple of 3 and instead
  of putting 16 I put 15 so that it just doesn't print it.
  ----------------------------------------------------------------------------------------------------------------------
  #Exercise 4. Multiplication Table Generator
#Create a function show_table(number) that prints the multiplication table of the given number from 1 to 10. Ask for a number, pass it as an argument, and call the function.
#Hint: Inside the function, use for i in range(1, 11). Multiply number by i

number = int(input("Give a number: "))
def show_table(number):
  for i in range(1, 11):
    print(number, " x ", i, " = ", number*i)

show_table(number)

#I got the range of i, then inputted it into an sentence, then inputted the code for multiplication to get the product at the end.
