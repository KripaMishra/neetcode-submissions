class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana1 = list(s)
        t_list = list(t)
        for item in ana1:
            if item in t_list:
                t_list.pop(t_list.index(item))
        return True if len(t_list)==0 else False