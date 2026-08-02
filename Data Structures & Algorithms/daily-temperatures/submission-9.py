class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r  = [0]*len(temperatures)
        stack= [] # it will store tuples of temp, idx
        for t,i in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stack