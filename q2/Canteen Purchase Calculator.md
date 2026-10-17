presyo = int(input("Enter item price: "))
ilan = int(input("Enter quantity: "))
mabayad = int(input("Enter amount paid: "))

def calculate_total(presyo, ilan):
  return presyo * ilan

def calculate_change(mabayad, total):
  return mabayad - total

total = calculate_total(presyo, ilan)
barya = calculate_change(mabayad, total)

print("Total: PHP", total)

if mabayad < total:
  kulang = total - mabayad
  print("You lack: PHP", kulang)
else:
  print("Change: PHP", barya)

#Documentation Questions
#1. What does each function do?
#Calculate_total(): Gets the total price
#calculate_change(): Subtracts total from the payment
#(mabayad - total) calculates for change
#2. What is the difference between the parameters price and quantity and the actual arguments passed to the function? 
#Parameters: only exist inside the function
#Arguments: are the actual values
#3. Where is the returned total stored, and how is it reused?
#It's saved in total variable

#4. Why is it useful to separate total calculation from change calculation?
#It keeps thing organized.
