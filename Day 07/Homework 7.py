from datetime import time

user_name = "Max"
user_age = 16
user_height = 1.70
user_weight = 60
bros_school_starts = time(8, 30)
he_is_on_time = bros_school_starts < time(8, 30)

# Display sentences
print("My brother " + user_name + " is " + str(user_age) + " years old.")
print("He is " + str(user_height) + "m tall and weighs " + str(user_weight) + "kg.")
print("His school starts at: " + str(bros_school_starts) + ". He is often on time, am I right, my PC? PC: " + str(he_is_on_time))

# Display the type of each variable
print(type(user_name))
print(type(user_age))
print(type(user_height))
print(type(bros_school_starts))
print(type(he_is_on_time))
