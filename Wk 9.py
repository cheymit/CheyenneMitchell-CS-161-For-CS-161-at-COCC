print("#1.")

class Students:     #class is named Students
    def __init__(self, name, age, grade): #creating a new instance "initializer method" the purpose is to initialize or set what the parammeters are
        self.name = name #this is the first parameter refers to the instance (every method in a class needs "self")
        self.age = age  #parameter
        self.grade = grade  #parameter

    def __str__(self):     #string representaion used to define an object. prints in this order
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


student1 = Students("James", 17, "11th")  #creating instances (objects) of the Students class specifications
student2 = Students("Sharon", 16, "11th")

print(student1) #prints the details of student1 objects
print(student2) #prints the details of student1 objects

print() #blank



print("#2.")

#Class 1 - Parent Class
class Staff: #class is named Staff
    def __init__(self, name, department, role, salary): #creating a new instance "initializer method" the purpose is to initialize or set what the parammeters are
        self.name = name #parameter
        self.department = department #parameter
        self.role = role #parameter
        self.salary = salary #parameter

    def __str__(self):  #string representaion used to define objects in this specific order
        return f"Name: {self.name}, Department: {self.department}, Role: {self.role}, Salary: {self.salary}"

#Class 2 - Child Class (inherits info form parent class)
class Teachers(Staff): #child class called Teachers
    def __init__(self, name, department, role, salary, age):
        super().__init__(name, department, role, salary) #from parent class
        self.age = age #new parameter

    def __str__(self): #string representaion used to define an object. prints in this order
        return f"Name: {self.name}, Age: {self.age}, Role: {self.role}, Department: {self.department}"
teacher1 = Teachers("Mitchell", "Science", "Teacher", 50000, 20)
teacher2 = Teachers("Cheyenne", "Math", "Teacher", 55000, 58)

print(teacher1) #prints the details of the teacher 1
print(teacher2) #prints the details of the teacher 2

print() #blank



print("#3.")

class Square:
    def __init__(self, side_length):  #creating a new instance "initializer method" the purpose is to initialize or set what the parammeters are
        self.side_length = side_length

    def area(self): #Calculates and returns the area of the square - i had to google the how to get an equation to find the area
        return self.side_length ** 2

    def perimeter(self): # Calculates and returns the perimeter of the square - i had to google the how to get an equation to find the area
        return 4 * self.side_length

square1 = Square(10) #length side of square1 =10
square2 = Square(20) #length of side of square2 = 20

print(f"The Area of square1 is: {square1.area()}") # Prints the area and perimeter of square1
print(f"The Perimeter of sqaure1 is: {square1.perimeter()}")

print(f"The Area of square2 is: {square2.area()}") # Prints the area and perimeter of square2
print(f"The Perimeter of sqaure2 is: {square2.perimeter()}")