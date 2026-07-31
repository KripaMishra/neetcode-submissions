class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = [] # pair of temperatures and indexes (29, 0) it is a tuple
        for idx, temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                ptemp,pidx  = stack.pop()
                result[pidx]= idx - pidx
            stack.append((temp,idx))
        return result