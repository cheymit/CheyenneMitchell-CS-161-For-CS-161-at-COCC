print("Hi,")
print("Welcome to my program!")
print() # This is a blank line

pet_type = "cat"
pet_name = "Yeti"
print("I have a " + pet_type + " and her name is " + pet_name + ".")
print() # This is a blank line

Character_name = "Alice"
num1 = 20
num2 = 1200
num3 = 10
num4 = 5
num5 = 6000
print(f"Hello {Character_name}! You are currently {num1} years old.")
print(f"In {num3} years, you will be {num1 + num3} years old.")
print(f"If you save ${num2} each year, in {num4} years you will have saved ${ num4 * num2}.")
print(f"Your average monthly savings is ${num2 * num4}.00.")
print() # This is a blank line

num_days = 31
num_hours = 24
num_mins = 60
num_secs_inhour = num_hours * num_mins
day_secs = num_secs_inhour * num_mins
print(f"Januaray has {num_days} days.")
print(f"There are { num_hours *num_mins } minutes, and {num_secs_inhour * num_mins} seconds in one day")
print(f"So in total there are { day_secs * num_days } seconds in the month of January.")
print() # This is a blank line

num_eggs = 37
dozens = num_eggs // 12
left_over_eggs = num_eggs % 12
print(f"There are {dozens} dozen eggs with {left_over_eggs} left over")
