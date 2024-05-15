for row in range(1,7):
    for spac in range(1, 7//2): 
        print("\t")
        for col in range (spac,row):
            print("#", end="\t")
    print()