print("#1: ")
def find_average(num1, num2, num3):
    '''
    Find the average of three numbers.

    Paramaters:
    num1 (int or float): first number
    num2 (int or float): second number
    num3 (int or float): third number

    Returns:
    float: the average of three numbers.
    '''
    average = (num1 + num2 + num3)/3
    return average

#input numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
#calculate
average = find_average(num1, num2, num3)

#print the result
print(f"The average is: {average}")

print() #blank


print("#2.")

#input numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
#calculate
average = find_average(num1, num2, num3)

#print the result
print(f"The average is: {average}")
def find_average(num1, num2, num3):
    '''
    Find the average of three numbers.

    Paramaters:
    num1 (int or float): first number
    num2 (int or float): second number
    num3 (int or float): third number

    Returns:
    float: the average of three numbers.
    '''
    average = (num1 + num2 + num3)/3
    return average

print("#This code will run when saved in same file as quesion one because python can recall from previous lines but can lead to inconsistancies")

print() #blank

print("#3.")
''' The script will not run because it doesnt like the parameter outside of the function.'''
print(" The script will not run because it doesnt like the parameter outside of the function.")
print() #blank


print("4.")
#user to enter their dogs age
print("Dog years equivalency to human years")
dog_age = int(input("Enter your dogs age: "))

def dog_human_years(dog_age):
    '''
    Conver a dogs age in human years

    Paramaters:
    dog_age (int): The age of the dog in human years

    Reuturns:
    int: the equivilent age in human years
    '''
    human_years = int(24 + (dog_age - 2) *  4)
    return human_years

print(f"{dog_age} dog years is equivilent to {dog_human_years(dog_age)} human years.")
print() #blank

print("5.")
# Calculate the depreciation for each car type
def calculate_car_value(purchase_price, years, car_type):
    ''''
    Calculate the future value of a car after a certain nu,ber of years, accounting for depreciation or appreciation based on car type.

    Parameters:
    purchase_price (float): initial purchse price.
    years (int): number of years owned.
    car_type (str): car type ('German', 'Japanese', 'Italian').

    Returns:
    float: calculated value of car after years owned

    Raises:
    ValueError: If an unknown car type is provided.
    '''

    #case sensitivity in car_type input
    car_type = car_type.capitalize()


#define depreciation and appreciation rates based on car type
    if car_type == "German":
        rate = -0.05  # Depreciation for German cars
    elif car_type == "Japanese":
        rate = -0.07  # Depreciation for Japanese cars
    elif car_type == "Italian":
        rate = 0.05   # Appreciation for Italian cars
    else:
        raise ValueError("Unknown car type. Please specify 'German', 'Japanese', or 'Italian'.")

    # Calculate car value after the specified number of years
    car_value = purchase_price * ((1 + rate) ** years)
    return car_value

# User inputs
car_type = input("Enter your car type (German, Japanese, Italian): ")
purchase_price = float(input("Enter the purchase price of the car: "))
years = int(input("Enter the number of years: "))

# Calculate and print car value
try:
    future_value = calculate_car_value(purchase_price, years, car_type)
    print(f" The value of your {car_type.capitalize()} car will be ${future_value:.2f} after {years} years.")
except ValueError as error:
    print(error)
print() #blank

print("6.")
def convert_to_human_years(dog_age):
    '''
    Convert a dogs age in human years

    Paramaters:
    dog_age (int): The age of the dog in human years

    Reuturns:
    int: the equivilent age in human years
    '''
    human_years = int(24 + (dog_age - 2) * 4)
    return human_years

#user to enter their dogs name and dog age
print("DOG AGE CALCULATOR:")
print("Lets find out how old your dog is in human years!")
dog_name = input("Enter your dogs name: ")
dog_age = int(input("Enter your dogs age: "))
human_years = convert_to_human_years(dog_age)
print(f"Your dog, {dog_name}, is {human_years} human years old.")
print() #blank

