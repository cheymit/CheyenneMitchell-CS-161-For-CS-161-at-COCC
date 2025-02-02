print("#3. This script will not run because python needs to see what to print after the parameters are defined.")
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

#input numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
#calculate
average = find_average(num1, num2, num3)

#print the result
print(f"The average is: {average}")
