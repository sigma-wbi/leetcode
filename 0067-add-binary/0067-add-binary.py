class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res10 = int(a,2) + int(b,2)
        res2 = format(res10,'b')
        
        return res2