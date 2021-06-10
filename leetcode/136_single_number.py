'''
https://leetcode.com/problems/single-number/
time complexity -> O(n)
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = set()
        for num in nums:
            if num in unique:
                unique.remove(num)
            else:
                unique.add(num)
        return unique.pop()