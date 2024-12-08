import os
import datetime
#create a new File
def create_file(filename):
    try:
        with open(filename,'w') as f:
            f.write(f'process started !!! {datetime.datetime.now()}\n')
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
    except FileNotFoundError:
        print("File Not Found")
    except IOError:
        print(f"Error: could not read file {filename}")
# append to a file
if __name__ == '__main__':
    source_filename = 'logfile.txt'
    # destination = 'destination.txt'

    create_file(source_filename)
    read_file(source_filename)