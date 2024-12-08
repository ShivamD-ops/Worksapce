def user_input_max():
    nums = input("""Enter List of Numbers with "<space>" seperated : """)
    nums = [int(i) for i in nums.split(' ')]
    return max(nums)

def max_list(arr):
    return max(arr)

sample = [2,3,5,1,3,77,8,9,0,55]
print(f"Max element in {sample} is ",max_list(sample))

#to modify finction for the smallest number in the list we will 
# change Max keyword to min
def min_list(arr):
    return min(arr)
