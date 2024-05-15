name="TECHNOLAB"
print(name[1])
print(name[1:4])
print(name[:7])
print(name[2:])
print(name[6:])
print(name[-1:-4:-1])
print(name[:-5:-1])
print(name[::-1]) #reverssed string
print(name[len(name)-2:])

word="madam"
rs=word[::-1]
print("palingdrome" if word==rs else "not palindrome")
