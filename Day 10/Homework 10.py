#1) Write a program that takes an input from the user and checks if it's a positive, negative, or zero number using if-else.
#2)Write a program that prints all the even numbers between 1 and 20 using a for loop and if statement.
#3)Write a program that calculates the sum of a number entered by the user using a while loop.
#4)Write a program that simulates a basic ATM. It should ask the user for their PIN, and if it's correct, display a text withdrawal, deposit, and balance.
#5)Write a program that simulates a simple login system. Ask the user for a username and password,
# and if they enter "admin" and "password123", respectively, print "Login successful" using if-else.
#6) Write a program that asks the user for their age and prints a message based on the age range (e.g., "Child", "Teenager", "Adult") using if-elif-else.

#1) Write a program that takes an input from the user and checks if it's a positive, negative, or zero number using if-else.
num = int(input("please state your number"))
if num > 0:
  print("this number is positive")
elif num < 0:
  print("this number is negative.")
else:
  print("this number equalts zero.")

#2)Write a program that prints all the even numbers between 1 and 20 using a for loop and if statement.
for i in range(1,21):
  if i % 2 == 0:
    print(i," is even")
  else:
    print(i," is odd")
#3)Write a program that calculates the sum of a number entered by the user using a while loop.

#4)Write a program that simulates a basic ATM. It should ask the user for their PIN, and if it's correct, display a text withdrawal, deposit, and balance.

options = ["withdrawal","deposit","balance",]
atm_pin = "123"
authorized = False

while authorized == False:
  login = input("please enter your pin: ")
  
  if login == atm_pin:
    print("Access Granted")
    authorized = True
  else:
    print("wrong pin, please try again.")
print("U can dive in")
print(options)
#5)Write a program that simulates a simple login system. Ask the user for a username and password,
# and if they enter "admin" and "password123", respectively, print "Login successful" using if-else.

username = "james123"
password = "smith123"

entered_username = input("Please enter username: ")

if entered_username == username:
    entered_password = input("Please enter password: ")
    if entered_password == password:
        print("Password is correct.")
        print("Access Granted.")
    else:
        print("Incorrect password. Access denied.")
else:
    print("Invalid username. Access denied.")



#6) Write a program that asks the user for their age and prints a message based on the age range (e.g., "Child", "Teenager", "Adult") using if-elif-else.

ask_age = int(input("please declare your age: "))

if ask_age < 13:
  print("you are a child")
elif ask_age > 13 and ask_age < 19 :
  print("you are a teenager")
else:
  print("you are an adult")
