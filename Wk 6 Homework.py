from operator import truediv

from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK
from selectors import SelectSelector

print("#1.")
print("Enter a number to begin count down")
x = int(input(":"))

while x > 0: #integer is greater than 0
    x = x -1 #counts down to 0 from interger
    print(x)

print("Blast off!!!")
print() #blank

print("#2. Even Odd")
print("Enter a number to begin count down")
x = int(input(":"))

while x > 0: #int greater than 0
    if x % 2 == 0: #checks if x is even
        print(f"{x} is even")
    else: # if its not even, if it is odd
        print(f"{x} is odd")
    x = x - 1 #counts down to 0

print("BLASTOFF!!!")

print() #blank

print("#3. All Odd")
print("Enter a number to begin count down")
x = int(input(":"))

print("Enter the amount of decrease")
decrease = int(input(":"))

while x > 0: #int greater than 0
    if x % 2 == 0: #checks if x is even
        print(f"{x} is even")
    else: # if its not even, if it is odd
        print(f"{x} is odd")
    x = x - decrease #decrease by the specified amount

print("Blast off!")

print() #blank

print("#4.1")
while True:
    word = input("Enter a word: ")
    if len(word) < 5:
        print("goodbye.") #if there are less than 5 letters in the word it will print goodbye
        break #after it prints goodbye, it stops
    else:
        print(f"{word} has {len(word)} letters")

print() #blank

print("#4.2")
word_count = 0
while True:
    word = input("Enter a word: ")
    word_count += 1
    if len(word) < 5: #if there are less than 5 letters in the word it will print goodbye
        print("goodbye.")
        break #after it prints goodbye, it stops
    elif word_count > 5: #after enter five 5 letters words it will print loser
        print("loser")
        break #after it prints loser, it stops
    else:
        print(f"{word} has {len(word)} letters")

print() #blank

print("#5")
decimal = 10 #start counting from
while decimal <= 100: #count up to
    binary = bin(decimal) #conerts in binary
    hexadecimal = hex(decimal) #count in hex
    print(f"{decimal} {binary} {hexadecimal}")
    decimal += 1 #counts up by 1

print() #blank

print("#6")
def print_stars_iterative():
    x = int(input("Enter a number: "))
    while x > 0: #using while function to achieve iterative
        print('*' * x) #print nuber of star to amount entered by useer
        x -= 1 #decreases the number of stars by 1

print_stars_iterative()


def print_stars_recursive():
    def helper(x): #helper checks if greater than 0 if so it will print stars
        if x > 0:
            print('*' * x) #print nuber of star to amount entered by useer
            helper(x - 1) #decreases the stars by 1

    x = int(input("Enter a number: "))
    helper(x)

print_stars_recursive()

print() #blank

