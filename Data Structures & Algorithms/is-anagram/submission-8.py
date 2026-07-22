class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = list(s)
        tl = list(t)
        if len(sl)==len(tl):
            for n in set(tl):
                if tl.count(n) != sl.count(n):
                    return False
            return True
        return False