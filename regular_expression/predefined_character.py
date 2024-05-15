from re import *

text="ab Cak7@#"
pattern="\d" #[0-9]
pattern="\D"  #[^0-9]
pattern="\W" #[a-zA-Z0-9] alphanumeric

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(), m.group())