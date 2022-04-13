#Printing Variable
from tkinter import N


name = "caleb stewart"
print(name.title())
print(name.upper())
print(name.lower())

fname = " caleb "
lname = "stewart"
full_name = fname.strip() + " " + lname
print("\n" + full_name.title())

#Line Break
print("\n")

#Printing Intergers
numadd = 4 + 4
numsub = 4 - 4
nummult = 4 * 4
numdev = 4 / 4
CONSTANT_4 = 4
print("Intergers of 4 and 4")
print("Adding: " + str(numadd))
print("Subtracting: " + str(numsub))
print("Multiplying: " + str(nummult))
print("Deviding: " + str(numdev))
print("To the power of: " + str(4 ** 4))
print("Order of Operations: " + str((4 + 4) * 4))
print("Decimals: " + str(.4))
x, y, z = 1, 5, 10
print(x)
print(y)
print(z)
print(str(CONSTANT_4 + 4))