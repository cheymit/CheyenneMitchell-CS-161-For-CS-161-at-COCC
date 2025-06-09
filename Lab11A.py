#This lab is based on exercise #39 on page 609 in the text:
"Suppose your job is to supervise the loading of two trucks, each of which can carry, at most, fourteen tons.  The cargo is a variety of crates whose total weight is twenty-eight tons but whose individual weights vary from crate to crate. The weight of each crate is marked on its side. What heuristic would you use for dividing the crates between two trucks?"

#A. Use the following code to start a program that solves this problem:

# === LAB 11A ===
# A. Basic Heuristic
# B. Check both trucks
# C. Test with different lists
# D. Sort cargo ascending
# E. Sort cargo descending
# F. Improved Algorithm
# G. Test classmate-breaking list


cargo = [9, 7, 3, 4, 5]
cargo.sort(reverse=True)  # large crates first
truck1, truck2 = [], []

for crate in cargo:
    if sum(truck1) <= sum(truck2):
        if sum(truck1) + crate <= 14:
            truck1.append(crate)
        else:
            truck2.append(crate)
    else:
        if sum(truck2) + crate <= 14:
            truck2.append(crate)
        else:
            truck1.append(crate)

print("Truck 1:", truck1, "Sum:", sum(truck1))
print("Truck 2:", truck2, "Sum:", sum(truck2))

