# Write a program to accept percentage from the user and display the grade according to the following criteria:
# Mark > 90 =A Grade
# >80 and <= 90 = B Grade
# >=60 and <= 80 =C Grade
# Below 60 = D grade

mark=int(input("enter the percentage of mark:"))
if(mark>90):
    print("A Grade")
elif(mark<=90 and mark>80):
    print("B Grade")
elif(mark<=80 and mark>=60):
    print("C Grade")
elif(mark<60):
    print("D Grade")