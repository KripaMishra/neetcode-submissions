class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        size =len(nums)
        while val in nums:
            for i in range(len(nums)):
                if nums[i] ==val:
                    nums.pop(i)
                    count +=1
                    break
                continue
        nums.sort()
        diff = size - count
        return diff