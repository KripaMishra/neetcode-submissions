class Solution:
    def longestCommonPrefix(self, strs:
List[str]) -> str:
        k = 1
        while k <= len(strs[0]):
            pfx = strs[0][:k]
            for word in strs:
                if word[:k] != pfx:
                    return pfx[:-1]

            k += 1

        return strs[0]