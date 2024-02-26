# შემოვაყვანინოთ მომხარებელს პაროლი და სანამ სწორ პაროლს არ შეიყვანს მანამდე დავაბრუნოთ საწყის გვერდზე

password = "123"
guess = input("please enter password: ")

while guess!= password:
    guess= input("please enter password: ")
print("Access granted!")

#_______________________________________________________________

password = "123"

guess = input("Password is: ? ")

while guess != password:
    guess = input("Password is: ? ")
    if guess == password:
        print("Access Granted")
    


password = "123"

guess = input("Password is: ? ")

while guess != password:
    guess = input("Password is: ? ")
    if guess == password:
        print("Access Granted")


# *** 3) იმუშავეთ, მაგალითები გააკეთეთ, range(), for, while, if else 
# თითო თემაზე 10 მაგალითი უნდა იყოს გაკეთებული სხვადასხვანაირად, ნამუშევარი ატვირთეთ github_ზე

for i in range (21):
    print("hello world")

for _ in range (0, 24):
    print(_ + 1)
    
for _ in range(24):
    print("Goa Rules")

sum_of_digits= 0

for i in range(10):
    sum_of_digits += i
print(sum_of_digits)    

for i in range(22):
    if i % 2 == 0:
        print(i,"is even")

for i in range(0,21):
    if i % 3 == 0:
        print(str(i) + " is odd")

sum_of_digits = 0
for i in range(11):
    sum_of_digits += i
print(sum_of_digits <= 11)

for i in range (21):
    print(i > 11)

age = 12
for i in range(12):
    print(i < i - 1)
    if i > i + 1:
        print("hello")
#---------------------------------------------------------------------
guess = 10
while guess + 1 < 14:
    print(True)
    guess += + 1
print("done")    

summoner_name = 123

while summoner_name < 125: 
    summoner_name += 1
    print("summoner name is ", True)
 
seats = 11
while seats > 0:
  print("Sell ticket")
  seats = seats - 1
print("Sold out")

seats = 5

while seats < 10:
    print("seats available")
    seats += 1

z = 0
while z < 3:
    if z == 0:
        print("z is", z)
    elif z == 1:
        print("z is", z)
    else:
        print("z is", z)
    z += 1


seats = 23

while seats < 30:
    print(30 - seats, " seats is left.")
    seats += 1
print("No more left.")  
