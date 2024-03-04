# 1)Write a program that prints numbers from 1 to 10 using a while loop.

i = 0
while i <= 10:
    print(i)
    i += 1

# 2)write a program that prints the even numbers from 1 to 10 using a for loop.

i = 0

while i <= 10:
  print(i)
  i+=1

# 3)Write a program that asks the user to enter a number and then prints whether the number is positive, negative, or zero using an if-else statement.

user_input= int(input("Please enter any number: "))

if user_input > 0:
  print("This number is positive.")
elif user_input <0:
  print("This number is negative.")
else:
  print("This is zero.")

# 4)Write a program that asks the user to enter a password. If the password is "abc123", print "Access granted"; otherwise, print "Access denied".

password= "abc123"

user_input = input("please enter your password: ")

if user_input == password:
  print("Access granted!")
else:
  print("Access Denied.")


# 5)Write a program that prints numbers from 1 to 10, but stops if the number is 5 using a while loop and the break statement. break

i= 0

while i < 10:

  i += 1
  print(i)

  if i == 5:

    break

# 6)Write a program that asks the user to enter a number between 1 and 5. If the number is less than 1 or greater than 5, print "Invalid input". If the number is between 1 and 5, print "Valid input".

user_input= int(input("Please enter number from 1-5: "))

if user_input > 5 or user_input < 1:
  print("Invalid input")
else:
  print("Valid input")



# 7)Write a program that asks the user to enter a number. If the number is divisible by 3, print "Fizz". If the number is divisible by 5, print "Buzz".
# If the number is divisible by both 3 and 5, print "FizzBuzz". Otherwise, print the number itself.

user_input = int(input("Please enter number: "))

if user_input % 3 == 0 :
  print("Fizz")
elif user_input % 5 == 0 :
  print("Buzz")
elif user_input % 3 == 0 and user_input % 5 == 0:
  print("FizzBuzz")
else:
  print(user_input)
