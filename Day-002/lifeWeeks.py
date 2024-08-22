age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line
# My solution👇
weeks_per_year = 52
age_limit = 90
ages_left = age_limit - int(age)
weeks_left = ages_left * weeks_per_year

print(f"You have {weeks_left} weeks left.")

# Angela's solution👇
age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")
