class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana1 = s.list()
        t_list = t.list()
        for item in ana1:
            if item in t_list:
                t_list.pop(item)
        return True if len(t_list)==0 else False