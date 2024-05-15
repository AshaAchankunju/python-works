word="pneumonoultramicroscopicsilicovolcanoconiosis"

#most freequent word

word_list=[ch for ch in word]
print(word_list)

for ch in word_list:
    if ch in word_list:
        m=word_list.count(ch)
        print(f"{ch} count={m}")