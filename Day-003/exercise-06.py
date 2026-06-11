# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Javier's Version 

combined_names = name1 + name2
combined_names = combined_names.lower()

# How many T R U E

true_count = 0
true_count += combined_names.count("t")
true_count += combined_names.count("r")
true_count += combined_names.count("u")
true_count += combined_names.count("e")

# How many L O V E

love_count = 0
love_count += combined_names.count("l")
love_count += combined_names.count("o")
love_count += combined_names.count("v")
love_count += combined_names.count("e")

score_string = str(true_count) + str(love_count)
love_score = int(score_string)

# Angela's version
# combined_string = name1 + name2
# lower_case_string = combined_string.lower()
# t = lower_case_string.count("t")
# r = lower_case_string.count("r")
# u = lower_case_string.count("u")
# e = lower_case_string.count("e")
# true = t + r + u + e
# l = lower_case_string.count("l")
# o = lower_case_string.count("o")
# v = lower_case_string.count("v")
# e = lower_case_string.count("e")
# love = l + o + v + e
# love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")       
