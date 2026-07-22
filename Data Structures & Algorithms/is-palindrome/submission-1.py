class Solution:
    def isPalindrome(self, s: str) -> bool:
        s  = "".join(char.lower() for char in s if char.isalnum())
        if len(s)<=1:
            return True
        middle = len(s)//2
        if len(s)%2==0:
            return s[:middle]==s[middle:][::-1]
        return s[:middle]==s[middle+1:][::-1]
