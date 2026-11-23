class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find how much rotated --> read the min. 
        for i in range(len(nums)-1):
            if not nums[i] < nums[i+1]:
                return nums[i+1]
        return nums[0]