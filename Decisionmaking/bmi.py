weight_in_kg=int(input("Enter weight in kg:"))
height_in_cm=int(input("enter height in cm"))

height_in_m=height_in_cm/100
bmi=weight_in_kg/height_in_m**2
print(bmi)

# if(bmi<=19):
#     print("under weight")
# elif (bmi>19 and bmi<=25):
#     print("healthy")
# elif(bmi>25 and bmi<=30):
#     print("overweight")
# elif(bmi>30 and bmi<=40):  
#     print("obesity")
# elif(bmi>40):
#     print("severe obesity")
if(bmi<=19):
    print("under weight")
elif ( bmi<=25):
    print("healthy")
elif( bmi<=30):
    print("overweight")
elif(bmi<=40):  
    print("obesity")
elif(bmi>40):
    print("severe obesity")