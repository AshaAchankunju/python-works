expenses=[12000,13000,23000,24000,25000,35000]
for i in range(0,len(expenses)):
    # if expenses[i]<25000 and expenses[i]>15000:
    #     print(expenses[i])
    if expenses[i] in range(15000,25000):
        print (expenses[i])