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
