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
    
     
