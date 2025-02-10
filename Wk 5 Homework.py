print("#1.")
print("Lets fund out if a number is divisble by 5.")
#enter a number
num1 = int(input("Enter a number: "))

#is it divisible by 5. use % to calculate if has remainder and == to set equal to 0
is_divisible_by_5 = (num1 % 5 == 0)

#print results true false statement
if is_divisible_by_5:
    print("True, the number is divisble by 5!")
else:
    print("False, the number is NOT divisble by 5.")
print() #blank line


print("#2.3.1 - if/elif/else")
print("Enter one of the following State names and I will tell you the capitol of that state!")
print("Oregon, Washington, California, Idaho, Nevada, Texas")
state_name = (input(":"))

if (state_name == 'Oregon'):
    print("Salem")
elif (state_name == 'Washington'):
    print("Seattle")
elif (state_name == 'California'):
    print("San Fansisco")
elif (state_name == 'Nevada'):
    print("Las Vegas")
elif (state_name == 'Texas'):
    print("Austin")
elif (state_name == 'Idaho'):
    print("Boise")
else:
    print("I dont know that one.")
print() #lank

print("#2.3.2 - Dictionary Approach")
'''name of dictionary and contents
convestion dictionary states to capitals'''
capitalconversion  = {
    "Florida" : "Tallahassee",
    "Louisiana" : "Baton Rouge",
    "Nebraska" : "Lincoln",
    "New Hampshire" : "Concord",
    "Pennsylvania" : "Harrisburg",
    "Wyoming" : "Cheyenne!!!"
}
'''ask for name of state'''
print("Enter one of the following State names and I will tell you the capitol of that state!")
print("Florida, Louisiana, Nebraska, New Hampshire, Pennsylvania, Wyoming")
state_name = input(":") #created a variable to use in conversion

'''converting the name and then calling upon the dictionary to print from it'''
capital = capitalconversion.get((state_name),("enter a state form the list damn you."))
print(capital)
print() #blank


print("#2.3.3 - Match Case Approach")
print("Enter one of the following State names and I will tell you the capitol of that state!")
print("New Mexico, Kentucky, Alaska, Montana, North Dakota, South Carolina")
state_name = input(":") # Ask the user to enter a state name

# Use the match case to search by state name
match state_name:
    case "New Mexico":
        print("Santa Fe.")
    case "Kentucky":
        print("Frankfort.")
    case "Alaska":
        print("Juneau.")
    case "Montana":
        print("Helena.")
    case "North Dakota":
        print("Bismarck.")
    case "South Carolina":
        print("Columbia.")
    case _:
        print("I do not know that one.")
print() #blank

print("#3.")
def pool_admission(age):
    """
    Find the price of admission based on age.

    Parameters:
    age (int): The age of the person.

    Returns:
    int: Admission Price (without the dollar sign).
    """
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age < 60:
        return 6
    else:
        return 4

def main():
    """
    Main function prompt user age
     then print the admission price.
    """
    try:
        age = int(input("Enter your age: "))
        price = pool_admission(age)
        print(f"The admission price for a {age}-year-old is ${price}.")
    except ValueError:
        print("Please enter a valid age.")

if __name__ == "__main__":
    main()

print() #blank

print("#4.")
import requests

def count_substring(url, substring):
    """
    Fetch HTML content from bobcat site and counts the occurrences of a substring.

    Parameters:
    url (str): The URL of the webpage.
    substring (str): The substring to count.

    Returns:
    int: The number of occurrences of the substring in the HTML content.
    """
    response = requests.get(url)
    html_content = response.text
    return html_content.count(substring)

# Example usage
url = "http://coccbobcat.com"
substring = "160"
count = count_substring(url, substring)
print(f"The substring \"{substring}\" appears {count} times in the HTML source of {url}.")

print() #blank

print("#5.")
import psutil

def count_processes():
    """
    Counts the number of processes running on the system.

    Returns:
    int: number of processes running.
    """
    process_count = len(psutil.pids())
    return process_count

if __name__ == "__main__":
    process_count = count_processes()
    print(f'The number of processes running on your system is: {process_count}')

print() #blank