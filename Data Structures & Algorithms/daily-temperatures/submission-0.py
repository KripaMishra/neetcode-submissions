class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        k =0
        for i in range(len(temperatures)):
            while k <len(temperatures):
                if temperatures[k]>temperatures[i]:
                    result.append(k)
                else:
                    k+=1
        return result
