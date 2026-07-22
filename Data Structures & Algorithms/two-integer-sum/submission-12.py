class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): # let 0-3  [0, 1,2,3]
            for j in range(i+1, len(nums)): # 1-3 [1,2,3]
                if i!=j and nums[i] + nums[j] == target:
                    return [i,j]