
def hello_hai(fn):
    def wrapper():
        data=f"<b>{fn()}</b>"
        return data
    return wrapper


@hello_hai
def get_hello():
    return "hello"

@hello_hai
def get_hai():
    return "hai"

print(get_hello())
print(get_hai())

