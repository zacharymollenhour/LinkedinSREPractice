#Leet Code 3Sum
#Given an array nums of n integers, are there elements a,b,c in nums
#such that a + b + c = 0? Find all unique triplets in the array which gives
#the sum of zero
class Solution:
    def __init__(self, nums,res):
        self.nums = nums
        self.res = res
    def threeSumAdd(self):
        
        self.nums.sort()
        for i in range(len(nums)):
            if self.nums[i] > 0:
                break
            if i == 0 or self.nums[i - 1] != self.nums[i]:
                self.sumFunc(i)
        return res
    def sumFunc(self, i):
        lo = i + 1
        hi = len(nums) - 1
        while(lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            if sum > 0:
                hi -= 1
            else:
                res.append([nums[i],nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
nums = [-1,0,1,2,-1,-4]
res = []
solutionobj = Solution(nums,res)
print(solutionobj.threeSumAdd())