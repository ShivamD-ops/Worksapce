try:
    with open("source.txt", "r") as src_file:
        data = src_file.read()

    with open("destination.txt", "w") as dest_file:
        dest_file.write(data)
except FileNotFoundError:
    print("Error: The source file does not exist.")
except IOError:
    print("Error: There was an issue with file writing.")
finally:
    print("File operations completed.")

'''
1) If source file doesnot exist exception FileNotFoundError is triggered
2)  With statement ensures putting lock
and file is closed properly
3) Permission Error, OS ERROR, EOFError can occur
we can handle them by simply using except blocks

'''
