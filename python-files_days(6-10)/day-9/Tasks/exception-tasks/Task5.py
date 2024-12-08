try:
    file = open("output.txt", "w")
    file.write("Hello, world!")
except IOError:
    print("Error: Unable to write to file.")
finally:
    file.close()
    print("File closed.")


'''
1) as with is not used removal of finnaly will remain file opened
2) finally block is executed even on exception being raised
3) Sending logs of the system even on exceptio or ob success logs are needed and useful
 
'''