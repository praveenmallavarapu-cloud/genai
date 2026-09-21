# name variable    

import sys


name = "praveen reddy" # assigning string value to name variable 
print(name) # printing the value of name variable
print(id(name)) # printing the id of name variable
x = 10 # assigning integer value to x variable
print(x) # printing the value of x variable 

name = "swetha reddy" # assigning new string value to name variable
print(name) # printing the new value of name variable
print(id(name)) # printing the id of name variable
print(id(x)) # printing the id of x variable 

name ,age ,job = "nirvaan karthikeya reddy", 4, "ips" # assigning multiple values to multiple variables
print(name , age, job) # printing the value of name variable 

a ,b ,c = 10, 20, 30 # assigning multiple values to multiple variables
print(a, b, c) # printing the value of a variable

agent1 = agent2 = "james bond" # assigning single value to multiple variables
print(agent1) # printing the value of agent1 variable   
print(agent2) # printing the value of agent2 variable

aa = 10 # assigning integer value to a variable
Aa = 10 # assigning integer value to A variable

print(aa ,Aa) # printing the value of a and A variable

#list
fruits = ["apple", "banana", "cherry"] # assigning list value to fruits variable
print(fruits) # printing the value of fruits variable

#tuple
scores = (90, 80, 70) # assigning tuple value to scores variable
print(scores) # printing the value of scores variable       

#dictionary
employee = {"name": "praveen reddy", "age": 25, "job": "developer"} # assigning dictionary value to employee variable
print(employee) # printing the value of employee variable   

#set literal 
vowels = {"a", "e", "i", "o", "u"} # assigning set value to vowels variable
print(vowels) # printing the value of vowels variable


# type conversion
int_num = 104 # assigning integer value to int_num variable
float_num = 1.04 # assigning float value to float_num variable
total = int_num + float_num # adding int_num and float_num
print(total) # printing the value of total variable
print("Datatype of total:", type(total)) # printing the type of total variable

int_num = 15 # assigning integer value to int_num variable
str_num = "15" # assigning string value to str_num variable
total = int_num + int(str_num) # adding int_num and str_num after converting str
print("total explicit type conversion:", total) # printing the value of total variable
print(type(total)) # printing the type of total variable

a = 5
b = "5"

print(str(a)+ b) # explicit type conversion of b variable to integer and adding it to a variable

# print(object= separator= end= file= flush=)  


print("greet", "hello", "world!", sep=" ", end="\n" ) # printing hello world with separator and end
print ("helloworld!") # printing hello world
print("happy", "new", "year!", sep=".") # printing happy new year with separator and end

num1 = 10
print(num1) # printing num1 variable with string
num2 = 10.5
print(num2) # printing num2 variable with string
name = "praveen reddy"
print(name) # printing name variable with string
print(9)

x = 5
y = 10

print('The value of x is {} and y is {}'.format(x,y))
'''
#input() function
name = input("Enter your name: ")
print("Hello, " + name + "!")
print(type(name)) # printing the type of name variable

num1 = input('Enter a number: ')
print("You entered:", num1)
print(type(num1)) # printing the type of num1 variable

'''

#python operators

x= 10
y= 5

# arthemetic operators  
print("Arithmetic operators")
print("Addition:", x + y) # addition operator
print("Subtraction:", x - y) # subtraction operator
print("Multiplication:", x * y) # multiplication operator
print("Division:", x / y) # division operator  
print("Modulus:", x % y) # modulus operator
print("Exponentiation:", x ** y) # exponentiation operator
print("Floor Division:", x // y) # floor division operator

# comparison operators
print("Comparison operators")
a = 9
b = 6

print("a is equal to b:", a == b) # equal to operator
print("a is not equal to b:", a != b) # not equal to operator
print("a is greater than b:", a > b) # greater than operator
print("a is less than b:", a < b) # less than operator
print("a is greater than or equal to b:", a >= b) # greater than or equal to operator
print("a is less than or equal to b:", a <= b) # less than or equal to operator


# logical operators
print("Logical operators")
x = True
y = False   

print("x and y:", x and y) # logical and operator
print("x or y:", x or y) # logical or operator  
print("not x:", not x) # logical not operator
print("not y:", not y) # logical not operator
print("x and not y:", x and not y) # logical and operator with not
print("x or not y:", x or not y) # logical or operator with not
print("not x and y:", not x and y) # logical and operator with not
print("not x or y:", not x or y) # logical or operator with not
print("not x and not y:", not x and not y) # logical and operator with not

# bitwise operators
print("bitwise operators")
c = 10
d = 2  
print("c & d:", c & d) # bitwise and operator
print("c | d:", c | d) # bitwise or operator
print("c ^ d:", c ^ d) # bitwise xor operator
print("~c:", ~c) # bitwise not operator
print("c << 2:", c << 2) # bitwise left shift operator
print("c >> 2:", c >> 2) # bitwise right shift operator
print("d << 2:", d << 2) # bitwise left shift operator
print("d >> 2:", d >> 2) # bitwise right shift operator
print("~d:", ~d) # bitwise not operator
print("c & d:", c & d) # bitwise and operator
print("c | d:", c | d) # bitwise or operator


# assignment operators

m = 5
n = 10
print("# assignment operators")
print("m += n:", m + n) # addition assignment operator
print("m -= n:", m - n) # subtraction assignment operator
print("m *= n:", m * n) # multiplication assignment operator
print("m /= n:", m / n) # division assignment operator
print("m %= n:", m % n) # modulus assignment operator
print("m **= n:", m ** n) # exponentiation assignment operator
print("m //= n:", m // n) # floor division assignment operator
print("m &= n:", m & n) # bitwise and assignment operator
print("m |= n:", m | n) # bitwise or assignment operator
print("m ^= n:", m ^ n) # bitwise xor assignment operator
print("m <<= n:", m << n) # bitwise left shift assignment operator
print("m >>= n:", m >> n) # bitwise right shift assignment operator


#special operators
# membership operators  
print("membership operators")

x1 = "Hello, world!"
y1 = {1, 2, 3, 4, 5}
print("H" in x1) # membership operator
print("Hello" not in x1) # membership operator
print(1 in y1) # membership operator
print(6 not in y1) # membership operator


# identity operators
print("identity operators") 

num1 = 10
str1 = "Hello"
print(num1 is 10) # identity operator
print(num1 is not 10) # identity operator
print(str1 is "Hello") # identity operator
print(str1 is not "Hello") # identity operator
