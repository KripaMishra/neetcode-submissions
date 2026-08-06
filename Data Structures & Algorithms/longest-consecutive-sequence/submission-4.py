class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nset = set(nums)
        print(nset)
        lseq= 1

        ## Create a set of the existing nums, use it to check if it is the start of a seq, how ? if arr[i]-1 in nset: False
        # if found the start of the seqence then iterate and find out the next.next.next until you don't run out of elements, keep a counter for the number of times you found the .next and compare it with the longest seq var, if larger then replace, else move to the next one as in arr[i+1]
        for i in range(len(nums)):
            if nums[i]-1 in nset: # there is 1 lower thann that element that means it's not a staring element of a series
                continue # continue to the next element instead of breaking the entire loop
            # handle the `found first element of the series`
            j = 1
            while nums[i]+j in nset:
                j+=1
            if j>lseq:
                lseq=j
        return lseq
