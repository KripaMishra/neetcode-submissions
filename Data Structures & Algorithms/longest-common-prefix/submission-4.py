class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = 0 ## This is the len of the prefix
        pfx = strs[0][:k]
        while k <len(strs[0]):
            for i in strs:
                if i[:k]==pfx:
                    continue
                else:
                    return strs[0][:k-1]
            k +=1
            pfx = strs[0][:k]
        return str(pfx)
