text="pneumonoultramicroscopicsilicovolcanoconiosis"
v_count=0
# for ch in text:
#     if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         v_count+=1
# print(f"vowel count={v_count}")
# print(f"total number of characters={len(text)}")
        # or
for ch in text:
    if ch in["a","e","i","o","u"]:
        v_count+=1
print(f"vowel count={v_count}")
print(f"total number of characters={len(text)}")
