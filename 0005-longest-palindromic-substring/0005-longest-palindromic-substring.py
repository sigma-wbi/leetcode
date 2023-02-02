'''
런타임 에러
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = []
        if len(s) == 1:
            return s
        else:
            for i in range(len(s)-1):
                window = []
                window.append(s[i])
                str_window = ''.join(s for s in window)
                result.append(str_window)
                for j in range(i+1,len(s)):
                    window.append(s[j])
                    if window == window[::-1]:
                        str_window = ''.join(s for s in window)
                        result.append(str_window)

        temp_lst = []
        index = []
        for i in range(len(result)):
            temp_lst.append(len(result[i]))
        max_lst = max(temp_lst)
        index.append(temp_lst.index(max_lst))


        return result[index[0]]
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
    
        if len(s) < 2 or s == s[::-1]:
            return s
    
        result = ''
        for i in range(len(s)):
            result = max(result, expand(i, i), expand(i, i + 1), key = len)
        return result