try:
    n = int(input("Enter a number : "))
    res = 100/n
    print(res)
except (ZeroDivisionError,ValueError) as e:
    print(f"the {e} error occured")

print("Code Countinues to run")

# An exception will only be caught once. If the first exception matches the type, the second and so on will be skipped over, even they might be sub types.
