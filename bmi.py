# Body Mass Index Calculating
# Get values from user

weight = float(input("Enter your weight (Kg) :"))
height = float(input("Enter your height (Cm) :"))
bmi = weight / (height/100)**2

# Ranges

if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obesity")

