# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2 

if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Normal weight')
elif bmi < 30:
    print('Overweight')
elif bmi < 35:
    print('Obese')
else:
    print('Clinically Obese')

