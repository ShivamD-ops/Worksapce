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
            for line in f:
                print(line)
        # print(f"{contents}")
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

def modify_file(filename,old,new):
    try: 
        with open(filename,'r') as f:
            data = f.read()
            data = data.replace(old,new)
        with open(filename,'w') as f:
            f.write(data)
        print(f"Text appended to file {filename} successfully.")
    except IOError:
        print(f"Error: could not append file {filename}")




if __name__ == '__main__':
    filename = 'text_file.txt'

    create_file(filename)
    read_file(filename)
    append_file(filename,"New Content to Updated file. \n")
    append_file(filename,"New Content to Updated file. \n")
    append_file(filename,"New Content to Updated file. \n")
    append_file(filename,"New Content to Updated file. \n")
    append_file(filename,"New Content to Updated file. \n")
    read_file(filename)
    modify_file(filename,'New','Old')
    read_file(filename)