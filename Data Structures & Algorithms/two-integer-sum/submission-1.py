class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            needed = target - n 
            if not needed in seen:
               seen[n] = i
            return [i, seen[n]]