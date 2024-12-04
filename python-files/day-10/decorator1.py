def smart_devide(func):
    def inner(a,b):
        print(f"Deviding {a} by {b}")
        if b == 0:
            print("cannot devide")
            return
        return func(a,b)
    return inner

@smart_devide
def devide(a,b):
    print(a/b)

devide(2,5)
devide(2,0)

