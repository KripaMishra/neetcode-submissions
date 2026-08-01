class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} # {num: freq}
        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1 
        seen = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        
        return list(seen.keys())[:k]