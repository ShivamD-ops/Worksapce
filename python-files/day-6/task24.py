with open("example.txt","w") as file:
        file.write(f"starting line\n")
for i in range(1,20):
    with open("example.txt","a") as file:
        file.write(f"this is line {i}\n") 
with open("example.txt","r") as file:
    for line in file:
        print(line.strip())
        # print("\n")

# opening a file that does not
# exist creates a new file in the location 
# we tried opening file
