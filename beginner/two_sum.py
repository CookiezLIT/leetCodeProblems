
class Solution:

    def twoSum(self, nums, target):
        for count, value in enumerate(nums):
            
            if target-value in nums[count+1:]:
                return [count,nums[count+1:].index(target-value)+count+1]

c = Solution()
print(c.twoSum([2,7,11,15],9))
print(c.twoSum([3,2,4],6))
print(c.twoSum([3,3],6))