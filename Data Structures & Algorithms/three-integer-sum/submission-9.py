class Solution:
    def threeSum(self,nums: list[int]) -> list[list[int]]:
        solution = []
        nums.sort()
        i = 0
        while i <= len(nums)-3:
            if 0<i and nums[i]==nums[i-1]:
                i+=1
                continue
            j = i +1
            k = len(nums)-1
            while j <k :
                if nums[i]+ nums[j]+ nums[k]==0:
                    solution.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                elif nums[i]+ nums[j]+ nums[k]>0:
                    k-=1
                else:
                    j+=1
            i+=1
        return solution