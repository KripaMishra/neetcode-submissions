class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
      k = 0 # starting of the index where we want to fill valid nums
      for i in range(len(nums)):
        if nums[i]!=val: # found the valid number to be replaced at the next index 
          nums[k]=nums[i]
          k +=1 # increment the position to be filled bcs it was filled with a valid number just now. 
        # Dont' do anything for the case nums[i]==val. it will be overritten when we find a valid number
      return k 
