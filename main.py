print("Electricity Bill")

units = float(input("Enter the number of units cosumed: "))

if units < 50:
    cost_per_unit = 2.60
    tax = 25
elif units < 100:
    cost_per_unit = 3.25
    tax = 35
elif units < 200:
    cost_per_unit = 5.26
    tax = 45
else:
    cost_per_unit = 8.45
    tax = 75

bill = (units * cost_per_unit) + tax
print("Total Electricity Bill =₹", bill)
