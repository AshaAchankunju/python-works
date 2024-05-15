# 3. Write a program to calculate BMI and give message ‘’over weight,underweight,healthy’

weight=int(input("Enter the weight in kg: "))
height=int(input("enter the height in cm: "))

height_in_meter=height/100
bmi=weight/(height_in_meter**2)

if bmi<18.5:
    print("Underweight")
elif bmi>18.5 and bmi<24.9:
    print("Healthy")
elif bmi<25 and bmi>29.9:
    print("Overweight")
elif bmi>30:
    print("Obesity")