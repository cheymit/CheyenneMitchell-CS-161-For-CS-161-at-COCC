print("#1.")
phrase1 = input("Enter a phrase: ") #prompt user for phrase

phrase2 = input("Enter the phrase in all caps please: ") #prompt user again for phrase but in uppercase

if phrase2  == phrase1.upper(): #checks to see if the phrase is the same but in uppercase
    print("Stop Shouting")


print() #blank

print("#2.")
phrase = input("Enter a phrase: ")
vowels = "AEIOUaeiou"
num_of_vows = 0 #counts the variables, starts counting from 0 - we alway need to assign a counting start point

for letters in phrase: #looks at the letters in the phrase
    if letters in vowels: #determins if the letter is a vowel
        num_of_vows += 1 #adds a 1 every time finds a vowel

if num_of_vows == 0: #if the number of vowels is 0 then it will print the no vowels message, if it is a true statement it will print
    print("There are no vowels in the word you gave sill head.")
else: #if the if statement is false, if there are indeed vowels more than 0 in the word it will print the number of vowels that in the given phrase
    print("There are", num_of_vows, "vowels in", phrase, ".")


print() #blank

print("#3.")
word11 = input("Enter a word: ") #promt user for a word
word12 = input("Enter a second word: ") #prompt user for a second word

if word11 < word12: #saying if the first word IS LESS THAN (comes earlier in the alphabet) the second word, IS TRUE
    print("The word" ,word11, "comes before the word", word12) #then it will print this
else: #if the if statement is false
    print("The word", word12, "comes before the word", word11) #then it will prin this

print() #blank

print("#4.")
email1 = input("Enter your email address: ") #promt user for email adress
email2 = input("Confirm email adress:") #promt user for email adress again

if email1 != email2: #is saying that if it is TRUE email1 is not equal to email2 ...
    print("DOES NOT MATCH.") #than it will print this
else: #but then if that is FALSE and the email address do match..
    print("Thank you.") #then it will print this


print()#blank

print("#5.")
print("I could not get the answer. This is what AI gave me as answer: ")

import time

def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

# Measuring time for iterative factorial
def measure_iterative(n):
    start = time.perf_counter_ns()
    iterative_factorial(n)
    stop = time.perf_counter_ns()
    return stop - start

# Measuring time for recursive factorial
def measure_recursive(n):
    start = time.perf_counter_ns()
    recursive_factorial(n)
    stop = time.perf_counter_ns()
    return stop - start

# Input values
inputs = [3, 10, 25]

# Measuring time for each input
for value in inputs:
    iterative_time = measure_iterative(value)
    recursive_time = measure_recursive(value)
    print(f"Input: {value}")
    print(f"Iterative: {iterative_time} ns")
    print(f"Recursive: {recursive_time} ns")
    print()
