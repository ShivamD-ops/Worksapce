list1 = [i for i in range(1,11)]
list2 = [i*i for i in list1]
list3 = [i for i in list2 if i%2!=0]

print(f"list1 -> {list1},\nlist2 squares-> {list2}, \nlist3 squares only odd -> {list3}")

#to create the list of even numbers we will
# modify the if condition in list to
# if i%2 == 0