class Solution:
    def threeSum(self,nums: list[int]) -> list[list[int]]:
        solution = []
        nums.sort()
        i = 0
        while i <= len(nums)-3:
            j = i +1
            k = len(nums)-1
            while j <k :
                if nums[i]+ nums[j]+ nums[k]==0:
                    solution.append([nums[i], nums[j], nums[k]])
                    break
                elif nums[i]+ nums[j]+ nums[k]>0:
                    k-=1
                else:
                    j+=1
            i+=1
        return solution
