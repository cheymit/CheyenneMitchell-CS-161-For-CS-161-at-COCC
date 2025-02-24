from tokenize import blank_re

print("CS161 - WK 7 Python - Cheyenne Mitchell")

print()#blank

print("#1.")
print("Give me two numbers and I will tell you all the even numbers between them!")

lower_num = int(input("Enter the lower number: ")) #promt user for lower number
higher_num = int(input("Enter the higher number: ")) #promt user for higher number

print("The even numbers between", lower_num, "and", higher_num, "are: ") #need to print this statement first

for number in range(lower_num, higher_num + 1):  #created loop to go through the range from low to high nimbers
    if number % 2 == 0: #checks is number is even
        print(number, end=" ") #prints the even numbers


print() #blank
print()

print("#2.")
print("For my trick I will tell you the factor of a number!")

number = int(input("Enter a positive number please: ")) #prompt user for a positive number
divisor = 1 #variable divisor "The variable divisor is initialized to 1, which will be used to check each number up to the given integer.

print("The integers of", number, "are:") #indiated te start

while divisor <= number: #loop to check each number
    if number % divisor == 0: #checks to see if divisor is a factor of the given number
        print(divisor, end=" ") #prints the current divisor if its a factor end=" " ensures the factors are printed on the same line separated by spaces.

    divisor +=1 #divisor to check the next number

print() #blank
print()

print("#3.")
print("Continuing to amaze, I will now calculate the sum of your name! Thats right!")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            #alphabet list is representing the letter wehre is at the location 0
name = input("Enter your name: ").lower() #converts all the letters to lowercase like my alphabet list

sum_of_positions = 0 #this hold the total sum of the numeric positions of the letters.

for letter in name: #goes through each letter in the name
    position = alphabet.index(letter) #Finds the index of the letter in my list
    sum_of_positions += position #adds the position to the sum_of_positions

print("The sum of your name is: ", sum_of_positions)

print()

print("#4.")
print("Next lets practice Recursion WOOOOOOOO")
def print_squares(n, current=1): #This function will print the squares of all numbers starting from 1 up to the given number "n"
    if current > n: #if the current is greater than n, stop the recursion
        return
    else:
        print(current * current) #print the sqaure of the current number
        print_squares(n, current + 1) #recursively calls the function with the next number

number = int(input("Enter a number: ")) #pront user to enter a number

print_squares(number) #calls the recursive function with user-provided number

print()#blank

print("#5.")
print("And now for some TeePee Sorting!!!!!!")

def teepee_sort(nums):
    odds = [num for num in nums if num % 2 != 0]
    evens = [num for num in nums if num % 2 == 0] #these separate the list into odd and even numbers

    odds.sort() #sorts the odd numbers in ascending order
    evens.sort(reverse=True) #sorts the even numbers in descending order

    max_num = max(nums) #this will find the largest number

    if max_num in odds:
        odds.remove(max_num)
    else:
        evens.remove(max_num) #This will remove the largest number from the lists to avoid duplication

    sorted_list = odds + [max_num] + evens #Creates a final sorted list by combining the sorted lists with the largest nuber in the center

    return  sorted_list

unsorted_list = [19, 89, 74, 48, 43, 6, 31, 9, 92, 69]
sorted_list = teepee_sort(unsorted_list)

print("Unsorted List:", unsorted_list)
print("TeePee Sorted List:", sorted_list)

print()#blank







print("#6.")
print("I could not figure this out on my own. This is what chatgpt gave me an answer:")

def find_next_highest_number(digits):
    # Helper function to swap two elements in a list
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    # Helper function to reverse a list from start index to end
    def reverse(arr, start, end):
        while start < end:
            swap(arr, start, end)
            start += 1
            end -= 1

    # Find the rightmost digit which is smaller than the next digit
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    # If no such digit is found, that means the digits are in descending order
    # and no larger number can be formed
    if i == -1:
        return "No larger number can be formed"

    # Find the smallest digit on the right side of (i) which is larger than digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Swap the found digits
    swap(digits, i, j)

    # Reverse the digits after the position i
    reverse(digits, i + 1, len(digits) - 1)

    return "".join(digits)

# Prompt the user to enter a number
number = input("Enter a number: ")

# Convert the number into a list of characters (digits)
digits = list(number)

# Find and print the next highest number
result = find_next_highest_number(digits)
print("The next highest number is:", result)