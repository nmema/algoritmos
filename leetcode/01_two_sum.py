'''
https://leetcode.com/problems/two-sum/
time complexity -> O(n * log(n))
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in indices:
                return [i, indices[x]]
            else:
                indices[nums[i]] = i
