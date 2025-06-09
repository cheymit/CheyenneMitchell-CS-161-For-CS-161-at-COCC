#Python Lab 11b     	Loading Cargo with Randomized Lists
#This lab is an extension of Lab 11a.

#A.  In the previous lab, you entered the cargo list by hand.  In this lab, we will explore how you can generate a list at random.   Start by importing the random module and printing a random integer.

# === LAB 11B ===
# A–E Random Cargo Generation with User Input

import random

cargo = []
while sum(cargo) < 28:
    crate = random.randint(1, 28 - sum(cargo))  # fixes going over 28
    cargo.append(crate)

print("Cargo:", cargo, "Total:", sum(cargo))

total = int(input("Enter total cargo weight: "))
truck_capacity = total // 2

cargo = []
while sum(cargo) < total:
    crate = random.randint(1, total - sum(cargo))
    cargo.append(crate)

print("Cargo:", cargo, "Total:", sum(cargo))

if total % 2 != 0:
    print(f"Warning: Total cargo {total} is odd. Trucks may not be evenly loaded.")
truck_capacity = total // 2 + (total % 2)  # one truck gets the extra if needed
