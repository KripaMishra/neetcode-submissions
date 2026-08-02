class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = 0 ## This is the len of the prefix
        pfx = strs[0][:1] if k==0 else  strs[0][:k]
        while 0<k <len(strs[0]):
            #pfx= strs[0][:k]
            for i in strs:
                if i[:k]==pfx:
                    continue
                else:
                    return i[:k]
            k +=1
        return pfx
