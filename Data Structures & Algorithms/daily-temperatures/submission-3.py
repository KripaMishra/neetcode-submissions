class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            k =i+1
            # result.append(0)
            while k <len(temperatures):
                if temperatures[k]>temperatures[i]:
                    result.append(k-i)
                    break
                k+=1
            else:
                result.append(0)
                
        return result
