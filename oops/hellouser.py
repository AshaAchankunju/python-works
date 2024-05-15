
def smart_print(fn):
    def wrapper(user):              #def wrapper(user)
        user=f"hello {user}"            #data="hello"+ {fn(user)}
        return fn(user)                 #return data
    return wrapper                   #return wrapper


@smart_print
def morning_greeting(user):
    return f"{user} good morning "

@smart_print
def afternoon_greeting(user):
    return f"{user} good afternoon "

@smart_print
def evening_greeting(user):
    return f"{user} good evening "


print(morning_greeting("asha"))
print(afternoon_greeting("ammu"))
print(evening_greeting("anu"))


