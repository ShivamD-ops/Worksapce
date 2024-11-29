import os
#create a new File
def create_file(filename):
    try:
        with open(filename,'w') as f:
            f.write('Hello World !!! \n')
        print(f"File {filename} created successfully.")
    except IOError:
        print(f"Error: Could not create file {filename}")

#with : Automatic resource management
#read file contents
def read_file(filename):
    try: 
        with open(filename,'r') as f:
            contents = f.read()
        print(f"{contents}")
    except IOError:
        print(f"Error: could not read file {filename}")

# append to a file
def append_file(filename,text):
    try: 
        with open(filename,'a') as f:
            f.write(text)
        print(f"Text appended to file {filename} successfully.")
    except IOError:
        print(f"Error: could not append file {filename}")

# file rename
def rename_file(filename,new_filename):
    try: 
       os.rename(filename,new_filename)
       print(f"file {filename} renamed to {new_filename} successfully")
    except IOError:
            print(f"Error: could not rename file {filename}")

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"file {filename} deleted successfully")
    except IOError:
        print(f"Error: could not delete file {filename}")
# print("hi")
if __name__ == '__main__':
    filename = 'data.txt'
    new_filename = 'data-new.txt'

    create_file(filename)
    read_file(filename)
    append_file(filename,"New Content to Updated file. \n")
    read_file(filename)
    rename_file(filename,new_filename)
    read_file(new_filename)
    delete_file(new_filename)



