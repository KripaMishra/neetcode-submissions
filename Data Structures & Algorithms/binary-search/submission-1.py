class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)-1
        l = 0
        r = N
        while l<=r:
            m = l + ((r-l)//2)
            if nums[m]==target:
                return m 
            elif nums[m]<target:
                l = m+1
            else:
                r = m-1
        return -1 