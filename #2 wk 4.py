

print("#2.")
print("This code will not run successfully because python likes to see the parameters defined before they are called upon.")
print("Although, the code will run when saved in same file as quesion one because python can recall from previous lines but can lead to inconsistancies")
print() #blank
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