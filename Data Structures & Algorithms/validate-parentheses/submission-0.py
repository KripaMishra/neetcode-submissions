class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<=1:
            return False
        complementOf= {"(": ")", "{": "}", "[" : "]"}
        stack = []
        for i in range(len(s)):
            # element is starting brace
            if s[i] in complementOf.keys():
                stack.append(s[i])
            # element is ending brace by there is no starting element in the stack  
            elif len(stack)==0 and s[i] in complementOf.values():
                return False
            # element is ending brace
            else:
                if complementOf[stack[-1]] == s[i]:
                    stack.pop(-1)
                else:
                    return False
        
        return len(stack)==0