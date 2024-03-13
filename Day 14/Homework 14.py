"""დავალება1) შექმენით სია, რომელშიც შეიტანთ რიცხვებს 0-იდან 20-ის ჩათვლით (ხელით ჩაწერეთ, ციკლის გარეშე), ბოლოს დაპრინტეთ მთლიანი სია.
Create an array which will include numbers from 0 to 20 (write it manually, without loops), then print whole array.

დავალება2) შექმენით ახალი სია, რომელშიც შეიტანთ ლუწ რიცხვებს წინა სიიდან. ბოლოს დაპრინტეთ ეს სია.
Create a new array, which will include even numbers from the first array. Then print this new array.

დავალება3) შექმენით ახალი სია, შემდეგ 50-იდან 100-მდე ამ სიაში შეიტანეთ ყველა რიცხვი (დასერჩეთ python array append). ბოლოს დაპტინტეთ თქვენთვის სასურველი სიის ნაწილი უარყოფითი index-ების საშუალებით.
Create an array, then add numbers from 50 to 100 to it. In the end, print the part of this array with negatives indexes.

დავალება4) მომხმარებელს შეეკითხეთ ორი მთელი რიცხვი, შემდეგ ამ ორი ცვლადიდან for ციკლში უმცირესი ჩასვის start-ის, ხოლო უდიდესი end-ის პოზიციაზე, step არ გინდათ. ახლა ჩაურთეთ if statement და დაპრინტეთ მარტო ხუთის ჯერადები.
Ask user for two inputs and store them as variables, their type has to be int. Then use for loop, use lower number from this two variables as start, Higher number as end, you do not need step. After that, you'll have to use if statement to only print multiples of five.

დავალება5) შექმენით ახალი სია. შემდეგ მომხმარებელს შეეკითხეთ მისი ასაკი და თუ ასაკი 18-ზე მეტი იქნება, შეეკითხეთ მას სახელი. მეორე ინფუთის შემდეგ სახელი შეიტანეთ სიაში და დაპრინტეთ ის.
Create a new array. Ask user his/her age and if it will be over 18, ask him/her name. Then add this name to already created array and print it."""





# დავალება1) შექმენით სია, რომელშიც შეიტანთ რიცხვებს 0-იდან 20-ის ჩათვლით (ხელით ჩაწერეთ, ციკლის გარეშე), ბოლოს დაპრინტეთ მთლიანი სია.
# Create an array which will include numbers from 0 to 20 (write it manually, without loops), then print whole array.

from ast import Num


list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list1)
# დავალება2) შექმენით ახალი სია, რომელშიც შეიტანთ ლუწ რიცხვებს წინა სიიდან. ბოლოს დაპრინტეთ ეს სია.
# Create a new array, which will include even numbers from the first array. Then print this new array.

list2=[]

for i in list1:
    if i % 2== 0:
        list2.append(i)
    else:
        continue
    
print(list2)

# Create an array, then add numbers from 50 to 100 to it. In the end, print the part of this array with negatives indexes.

my_list=[50,60,80,90,100]

print(my_list[-1])
print(my_list[-2])

# Ask user for two inputs and store them as variables, their type has to be int. Then use for loop,
#  use lower number from this two variables as start, Higher number as end, you do not need step. 
# After that, you'll have to use if statement to only print multiples of five.
Num=int(input("num1: "))
num2=int(input("num1: "))
list5=[]
for i in range (min(Num,num2), max(num2,Num+1)):
    list5.append(i)


print(list5)

for num in (list5):
  if num % 5 == 0:
      print(num)

# print(list5)
# Create a new array. Ask user his/her age and if it will be over 18, ask him/her name. Then add this name to already created array and print it."""

list_new=[]
age=int(input("Your age please: "))

if age >18:
    user_name=input("your name please:")
    list_new.append(user_name)
    print(list_new)
else:
    print("Go Home.")


