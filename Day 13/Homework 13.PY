# 1) შექმენით სია, რომელშიც შეიტანთ რიცხვებს 0-იდან 20-ის ჩათვლით (ხელით ჩაწერეთ, ციკლის გარეშე), ბოლოს დაპრინტეთ მთლიანი სია.


num_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#2) შექმენით ახალი სია, რომელშიც შეიტანთ ლუწ რიცხვებს წინა სიიდან. ბოლოს დაპრინტეთ ეს სია.

even_list =[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



# 3) შექმენით ახალი სია, შემდეგ 50-იდან 100-მდე ამ სიაში შეიტანეთ ყველა რიცხვი (დასერჩეთ python array append). ბოლოს დაპrინტეთ თქვენთვის სასურველი სიის ნაწილი უარყოფითი index-ების საშუალებით.
fity_nums = [ 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
print(fity_nums[-10])
print(fity_nums[-25])
print(fity_nums[-49])
print(fity_nums[-51])
# Creating an empty list
my_list = []

# Appending elements to the list
my_list.append(1)
my_list.append(2)
my_list.append(3)

# Displaying the updated list

print(my_list,"before list")

for num in range (1,21):
  
  if num % 2 == 0:

    my_list.append(num)
print(my_list)

# # 4) მომხმარებელს შეეკითხეთ ორი მთელი რიცხვი, შემდეგ ამ ორი ცვლადიდან for ციკლში უმცირესი ჩასვიT start-ის, ხოლო უდიდესი end-ის პოზიციაზე,
# #  step არ გინდათ. ახლა ჩაურთეთ if statement და დაპრინტეთ მარტო ხუთის ჯერადები.
nums= [ 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 
       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
         86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

user_ask1 = int(input("Please enter number lower then 50: "))
user_ask2 = int(input("Please enter number higher then 100: "))

if user_ask1 < nums[0] and user_ask2 > nums[-1]:
  nums[0]=user_ask1
  nums[-1] = user_ask2
  print(nums,"As u can see", user_ask1,"is now before", nums[1],
        "as for", user_ask2, "now its after", nums[-2])
else:
  print("You can't do that!")


# შექმენით ახალი სია. შემდეგ მომხმარებელს შეეკითხეთ მისი ასაკი და თუ ასაკი 18-ზე მეტი იქნება, შეეკითხეთ მას სახელი. მეორე ინფუთის შემდეგ სახელი შეიტანეთ სიაში და დაპრინტეთ ის

names=["Jamal","James","Johnathan","JumboMambo"]

# ask= input("Please tell us your name: ")
ask_age=int(input("Please tell us your age: "))

if ask_age >18:
  ask= input("Please tell us your name: ")
  names.insert(-1,ask)
  print(names)
else:
  print("nononononononnononon")






