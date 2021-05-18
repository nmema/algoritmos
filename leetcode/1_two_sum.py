class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_sorted = sorted(nums)
        
        for i in range(len(nums_sorted) - 1):
            pivot = nums_sorted[i]
            pase = i + 1
            base = nums_sorted[pase]
            while (pivot + base) <= target:
                if (pivot + base) == target:
                    return [nums.index(pivot), nums.index(base)]
                else:
                    pase += 1
                    base = nums_sorted[pase]