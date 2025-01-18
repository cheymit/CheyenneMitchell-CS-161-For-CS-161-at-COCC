print("1.")
x = 31 #CHEN YOU NEED TO CUSTOMIZE THE VALUES
print (x, bin(x), hex(x)+  " - teacher example")
x = 82
print (x, bin(x), hex(x))
print() #blank line

print("2.")
print("the error code said object connot be iterpreted as an integer (in decimal).")
x = 18
print(x, bin(x), hex(x))
print() #blank line

print("3.")
y = 0b1011
z = 0xA3

print(y,z,hex(y), hex(z)+  " - teacher example")
y = 0b101011001
z = 0x49
print(y,z,hex(y), hex(z))
print() #blank line

print("4.")
w = x + y + z
x = 1
y = 2
z = 3
print ('the sum of 1,2,3 is' , w)
print() #blank line

print("COMPRESSION")
print("1. - teacher example")
og_size = 240
dictionary_size = 25
compressed_text = 148
percent = 100

num1 = (compressed_text + dictionary_size)
num2 = og_size
num3 = percent
print((1-(num1)/(num2))*num3)

phrase = "The percent of compression is approximately 27.92%"
print(phrase)
print(phrase [5].isalpha())
print() #blank line

print("2.")
og_size = 280
dictionary_size = 15
compressed_text = 97
percent = 100

num1 = (compressed_text + dictionary_size)
num2 = og_size
num3 = percent
print((1-(num1)/(num2))*num3)

phrase = "The percent of compression is approximately 60%"
print(phrase)
print(phrase [5].isalpha())
print() #blank line

print(":)")