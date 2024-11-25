#1
for i in range(1,11):
    print(f'{i}')
#2
for i in range(1,11):
    if i%2 != 0:
        continue
    print(f'{i}')
# 3
for i in range(1,11):
    if i == 7:
        break
    if i%2 != 0:
        continue
    print(f'{i}')
    
# WHEN continue IS EXECUTED LOOP SKIPS ALL THE CODE
# BELOW AND MOVES TO NEXT ITERATION
# WHEN break IS EXECUTED THE LOOP BREAKS OUT 
# FROM THE CURRENT BLOCK OF LOOP