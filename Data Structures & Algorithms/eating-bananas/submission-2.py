import math
from typing import List
"""
What are trying to do?
we have
    h: time constraint in hourse
    k : the variable value that we need to solve for, it represents how many bananas Koko can eat per hour.
    Approach:
        since we know the range of the output (k) we can just run a binary search on it. since we want to minimize k we need to store each valid value, and keep on updating it on a successfull pass by comparing it with the current rest. so at each pass we want to find the middle calculate the time taken and if it is valid(<h) then we compare with the k with the res and then update the res with the current k.
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (l+r)//2 # Middle of the range
            time_taken = 0 # Total time taken to eat all bananas at speed k
            for i in piles:
                time_taken += math.ceil(float(i)/k) # calculate the round-up time value for the
            if time_taken <= h: # compare the current calculated time with the time constraint
                res = min(res, k) # update with minimun of the two, (res, k)
                r = k - 1  # since the time taken is lesser than the constraint, we need to now move the active range to the left.
            else:
                l = k + 1 # since the time taken is higher than the constraint, we need to now move the active range to the right.
        return res