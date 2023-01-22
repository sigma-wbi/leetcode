class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        else:
            listx = list(str(x))
            while len(listx) > 1 :
                if listx.pop(0) == listx.pop():
                    continue
                else :
                    return False
        return True