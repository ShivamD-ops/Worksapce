try:
    with open("data.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
else:
    print("File content:\n", content)

'''
    1) if data.txt is not found the print("Error: File not found.") statement is executed
    2) With statement opens and closes the file automaticaly
    3) IOError can also occur and it can be handled by
       except IOError:
            print("Message")
'''

