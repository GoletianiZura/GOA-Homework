
#1)  Calculate the sum of all even numbers from 1 to 10 using a while loop:

num = 1
sum_of_evens = 0

while num <= 10:
    if num % 2 == 0:
        sum_of_evens += num
    num += 1

print("Sum of even numbers is:", sum_of_evens)

# 2) while ციკლის მეშვეობით შეამოწმეთ რიცხვები 1 დან 20 ჩათვლით, რიცხვი თუ იყოფა 3 და 5 ზე მაშინ დაპრინტეთ ეგ რიცხვი

num= 0

while num <=20:
    num += 1
    if num % 3 ==0 and num % 5 ==0:
        print(num)

#3) for ციკლის მეშვეობით დაბეჭდეთ ყველა რიცხვი 1-100 ჩათვლით რომელიც იყოფა 5 ზე
  
for i in range(1,100+1):
    if i % 5 ==0:
        print(i)

# 4) for ციკლის მეშვეობით დაბეჭდეთ ყველა ის ირცხვი რომელიც იყოფა 6_ზე 1 დან 20 ის ჩათვლით

for i in range(1,20+1):
    if i % 6 == 0:
        print(i)

