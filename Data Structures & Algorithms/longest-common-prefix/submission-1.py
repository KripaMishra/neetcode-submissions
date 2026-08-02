class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # selecting the prefix 
        # checking if all elements of arr contains
        # a While loop that increments the len of prefix to choose 
        #, while it is less than the len(str) itself. 
        # Do we first choose the prefix or select the str ?
        if len(strs)==0:
            return ""
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
        return pfx
