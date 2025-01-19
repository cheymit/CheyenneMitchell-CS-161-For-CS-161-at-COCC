from ctypes import HRESULT

print("1.")
num1 = input("enter variable for x: ")
num1 = int(num1)
print(num1, bin(num1), hex(num1))
print() #blank line

print("2.")
print("the error code said object connot be iterpreted as an integer (in decimal).")
num1 = input("enter variable for x: ")
num1 = int(num1)
print(num1, bin(num1), hex(num1))
print() #blank line

print("3.")
num1 = input("enter variable for y: ")
num2 = input("enter variable for z: ")
num1 = int(num1)
num2 = int(num2)
print((num1), (num2), bin(num1), hex(num2))
print() #blank line

print("4.")
num1 = input("enter variable for w: ")
num2 = input("enter variable for y: ")
num3 = input("enter variable for z: ")
num4 = float(num1)
num5 = float(num2)
num6 = float(num3)
result = (num4+num5+num6) #calculate the sum
print(result)
print() #blank line

print("COMPRESSION")

percent = 100
og_size = 240
num1 = input("Enter Compressed text size: ")
num2 = input("Enter Dictionary size: ")
num3 = percent
num4 = og_size
num5 = float(num1) + float(num2)

result = ((1-(num5)/(num4))*num3)
result = round(result, 2) #round to 2 decimal places
print("Results = " + str(result) + "%")
print() #blank line


