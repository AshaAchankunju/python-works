for row in range(1,6):
    for col in range(1,row+1):
        print("0" if col%2!=0 else "E", end="\t")
    print()