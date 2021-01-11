#Question 1 Two Sum
#Given an array of integers num and an integer target
#Return indices of the two numbers such that they add up to target
#Assume taht each input would have exactly one solution
#And you may not use the same element twice

def twoSum(nums, target):
    seen = {}
    
    for i, v in enumerate(nums):
        targetDifference = target - v
        if targetDifference in seen:
            return [seen[targetDifference], i]
        seen[v] = i
    return []

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))