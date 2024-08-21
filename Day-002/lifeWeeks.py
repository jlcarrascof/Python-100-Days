age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
weeks_per_year = 52
age_limit = 90
ages_left = age_limit - int(age)
weeks_left = ages_left * weeks_per_year

print(f"You have {weeks_left} weeks left.")
