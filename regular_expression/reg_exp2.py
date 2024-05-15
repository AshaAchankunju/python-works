from re import *

text="KaBbcC7 9@dE"
# pattern="[ac]" # either a or c in the text
# pattern="[a-e]" # mathes a b c d e
# pattern="[a-z]" # matches all lowercase alphabets
# pattern="[A-Z]" # matches all uppercase alphabets
# pattern="[A-Za-z]" # matches all alphabets
# pattern="[0-9]" # al digits from 0 to 9
# pattern="[^a-z]" # exclude a-z
# pattern="[a-zA-Z0-9]"
pattern="[^a-zA-Z0-9]"
matcher=finditer(pattern,text)
for obj in matcher:
    print(obj.start(),obj.group())