text="#@123pneumonoultramicroscopicsilicovolcanoconiosis"
c_count=0
for ch in text:
     if ch not in["a","e","i","o","u"]:
        if ch.isalpha():
            c_count+=1
print(f"consonents count={c_count}")
print(f"total number of characters={len(text)}")
