class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        There are two main cases:
        1. Empty list = []
        2. List with empty strings = [""]
        """
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res            
    def decode(self, s: str) -> list[str]:
            res = []
            i = 0
            
            while i < len(s):
                j = i
                # Find where the length ends (the '#' delimiter)
                while s[j] != '#':
                    j += 1
                
                # Extract the length of the string
                length = int(s[i:j])
                
                # Extract the actual string using the length
                i = j + 1
                res.append(s[i : i + length])
                
                # Move index past the current string
                i += length
                
            return res