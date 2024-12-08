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
def write_file(filename,text):
    try: 
        with open(filename,'w') as f:
            f.write(text)
        print(f"Text written to file {filename} successfully.")
    except IOError:
        print(f"Error: could not append file {filename}")

if __name__ == '__main__':
    filename = 'report.txt'

    create_file(filename)
    read_file(filename)
    write_file(filename,"New Content to Updated file. \n")
    read_file(filename)