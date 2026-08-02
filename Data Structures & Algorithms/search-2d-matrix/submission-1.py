class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lm = 0
        rm = len(matrix)-1
        mm = (lm + rm)//2 # This pointer will hold the row that we are checking. 
        while lm<=rm and 0<=mm<len(matrix):
            ca = matrix[mm]
            la = 0
            ra = len(ca)-1
            while la<=ra:
                ma = la+((ra-la)//2)
                if ca[ma]==target:
                    return True
                elif ca[ma] <target:
                    la=ma+1
                else: #ca[ma] > target
                    ra=ma-1  
            if ra>0:
                mm-=1
            else:
                mm+=1
        return False                  
