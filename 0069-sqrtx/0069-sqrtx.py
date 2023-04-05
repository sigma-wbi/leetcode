class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        for i in range(1,x+1):
            # 1부터 제곱하여 x와 비교
            square = i*i
            if square <= x :
                res = i
                continue
            else :
                break
                
        return res