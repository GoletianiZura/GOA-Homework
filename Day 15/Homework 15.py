"""
Homework: 

Write a program that takes asks user for number (use input). If number is even, print that number is even. Else print that number is not even, also print next even number, for example if input is 15, print 16.

Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". Also print the count of incorrect passwords.

Write a function that takes a string as input and returns True if first character of that string is "G".

Ask user for five names (use input five times). Add all of them in one list and print only first three names.

Write a function that checks if a given number is prime or not (prime number has only two divisors - გამყოფი) Use a for loop for this task.

Create a while loop that prints numbers from 10 to 0 (10-იდან 0-მდე).

Implement a simple calculator that takes two numbers and an operator (+, -, *, /) as input from the user and performs the corresponding operation. Bonus task if you want, it's not necessary - add degree (ხარისხი), use ** operator for it.

Ask user to enter name and print the last character of that string.

Using for loop, ask user for number. Then create a list which will have even numbers in next range: from 0 to user's number. At last, print out whole list. 

Ask user for whole number. Then create a factorial for this number and print it out (If you don't know what a factorial is, google it).
"""

# Write a program that takes asks user for number (use input). If number is even, print that number is even. 
# Else print that number is not even, also print next even number, for example if input is 15, print 16.


ask_user = int(input("Please input number: "))

if ask_user == 0:
    print("That's ZERO.")
else:
    if ask_user % 2 == 0:
        print(ask_user, " is even.\nNext even num is- ", ask_user + 2)
    else:
        print(ask_user, " is odd.\nNext odd num is- ", ask_user + 3)


# Create a while loop that asks the user to enter a password. Keep asking until they enter the correct password "Goa best". Also print the count of incorrect passwords.



authorize= False
password= "Goa best"
count=0

while authorize != True:
  ask_user=input("please enter pass: ")
  
  if ask_user == password:
    
    print("\nAccess Granted,\n"," incorrect answers ",count)

    authorize = True
  else:
    
    print("Access Denied", )
    count += 1

# Write a function that takes a string as input and returns True if first character of that string is "G"

ask=input("word please: ")

if ask[0:1] == "g" or ask[0:1] == "G":
  print("issa g class")
else:
  print("naaaa")
  

# Ask user for five names (use input five times). Add all of them in one list and print only first three names.
name1=input("Name1: ")
name2=input("Name2: ")
name3=input("Name3: ")
name4=input("Name4 :")
name5=input("Name5: ")

name_all= name1+name2+name3
print(name_all)

# Write a function that checks if a given number is prime or not (prime number has only two divisors - გამყოფი) Use a for loop for this task.

# Create a while loop that prints numbers from 10 to 0 (10-იდან 0-მდე).

i = 10

while i != 0:
  
  print(i)
  i -= 1
  
"""
Implement a simple calculator that takes two numbers and an operator (+, -, *, /) 
as input from the user and performs the corresponding operation.
Bonus task if you want, it's not necessary - add degree (ხარისხი), use ** operator for it.

"""
# Ask user to enter name and print the last character of that string.

ask_user=input("Name:")
print(ask_user[-1:])

# Using for loop, ask user for number. Then create a list which will have even numbers in next range: from 0 to user's number. At last, print out whole list. 

numb=[0]
ask_number= int(input("num:"))

for i in range(ask_number):
  

  print("evens in list- ",numb[::3])
  numb.append(i)
  # print(numb)

