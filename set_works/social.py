insta_users={"mohanlal","prithvi","dq","vijay","fahad","sureshgopi","lalu"}
mohanlal_followings={"prithvi","vijay","lalu"}
mohanlal_suggestions=insta_users.difference(mohanlal_followings)
mohanlal_suggestions.discard("mohanlal")
print(mohanlal_suggestions)

dq_friends={"prithvi","fahad","sureshgopy","lalu"}
mutual_friends=mohanlal_followings.intersection(dq_friends)
print(mutual_friends)