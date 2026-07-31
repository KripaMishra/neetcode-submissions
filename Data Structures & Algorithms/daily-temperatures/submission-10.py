class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        r  = [0]*len(temperatures)
        stack= [] # it will store tuples of temp, idx
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                # we need the current id of the stack. peek so that we can update insert the diff in the result at the idx index
                _, idx = stack.pop()
                # here we can insert the diff 
                r[idx]= i - idx
            stack.append((t,i))
        return r 