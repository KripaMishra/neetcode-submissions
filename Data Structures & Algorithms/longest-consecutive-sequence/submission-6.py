class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nset= set(nums)
        result  =1

        for i in range(len(nums)):
            # check if the 1 less is already in the set, meaning ths ith element is not start of a seq.
            if nums[i]-1 in nset:
                continue # finish the current iternation and move to the next item ie, i+1     
            # handle the start of a sequence
            j =1 # initializing j that will help iterate/find on next sequence element
            while nums[i]+j in nset: # note that here we don't need to add a limit on the j bcs we're only checking if an element is there in the set, not accessing it with the index. 
                j+=1
            if j>result:
                result = j 
        return result
