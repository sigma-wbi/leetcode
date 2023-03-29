class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res10 = int(a,2) + int(b,2)
        
        # 'b' : 2진수로 변환 'o' : 8진수로 변환 'x' : 16진수로 변환
        res2 = format(res10,'b')
        
        return res2