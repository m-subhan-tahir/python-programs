nums = [12,56,32,92,34,66,1,1001,99]

largestNum  = nums[0]

for index in range(len(nums)):
    if(largestNum < nums[index]):
        largestNum =  nums[index]
        
print(largestNum)