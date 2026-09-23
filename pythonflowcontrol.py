'''
#if and indentation in python

age = int(input("Enter your age: ")) # taking input from user and converting it to integer
if age >= 18: # checking if age is greater than or equal to 18
    print("You are eligible to vote.") # printing message if condition is true
    print("if statement executed") # printing message if condition is true20
print("Thank you for using the voting eligibility checker.") # printing message after if statement


age = int(input("Enter your age: ")) # taking input from user and converting it to integer
if age >= 18: # checking if age is greater than or equal to 18
    print("grant access to site.") # printing message if condition is true
else:
    print("access denied.") # printing message if condition is false
print("Thank you for using the site.") # printing message after if statement


username = "admin"    
password = "admin@123"

username_input = input("Enter your username: ") # taking input from user
password_input = input("Enter your password: ") # taking input from user

if username_input == username and password_input == password: # checking if username and password are correct
    print("Login successful!") # printing message if condition is true  
else:
    print("Login failed. Please check your username and password.") # printing message if condition is false
    
lovers = ["swetha" , "praveen"]

user_input = input("Enter your name: ") # taking input from user

if user_input == lovers[0]:
    print("marry") # printing message if condition is true
elif user_input in lovers[1] == "praveen":
    print(" marry") # printing message if condition is false 
else:
    print("not marry") # printing message if condition is false   
# greatest number     
n1 = int(input("Enter first number: ")) # taking input from user and converting it to integer
n2 = int(input("Enter second number: ")) # taking input from user and converting it to integer
n3 = int(input("Enter third number: ")) # taking input from user and converting it to integer

if n1 >= n2 and n1 >= n3: # checking if n1 is greater than or equal to n2 and n3
    print("The largest number is:", n1) # printing the largest number   
elif n2 >= n1 and n2 >= n3: # checking if n2 is greater than or equal to n1 and n3
    print("The largest number is:", n2) # printing the largest number   
else: # if both conditions are false
    print("The largest number is:", n3) # printing the largest number 
'''    
#for loop in python

models = ["BMW", "AUDI", "MERCEDES", "TOYOTA", "HONDA"] # list of car models
for model in models: # iterating through the list
    print(model) # printing each model in the list
    print("\n")





    