class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lm = 0
        rm = len(matrix)-1
        mm = (lm + rm)//2 # This pointer will hold the row that we are checking. 
        while lm<=rm and 0<=mm<len(matrix):
            # We will firts check the row for the element using the binary search, and if the element is not found 
            # in the internal while loop, we will increment or decrease the `mm` pointer to use the a previous or later array.
            ca = matrix[mm]
            la = 0
            ra = len(ca)-1
            while la<=ra:
                ma = la+((ra-la)//2)
                if ca[ma]==target:
                    return True
                elif ca[ma] <target:
                    la=ma+1
                else:
                    ra=ma-1  
            if ra<la:
                mm-=1
            else:
                mm+=1
        return False                  
