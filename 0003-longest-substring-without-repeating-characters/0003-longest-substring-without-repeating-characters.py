class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s = list(s)
        
        if len(s) == 0:
            return 0 
        
        count, longest = 1, 1
        for i in range(0,len(s)-1) :
            for j in range(i+1,len(s)) :
                if len(s[i:j+1]) == len(set(s[i:j+1])):   # 파이썬 set은 중복을 제거한다. 둘의 길이가 다르면 중복이 있다는뜻
                    count = len(s[i:j+1])
                    longest = max(longest,count)          # 지금 까지의 longest보다 count 값이 더크면 longest값 변경
                else:
                    count = 1                             # 중복 문자열이 있다는 의미이므로 카운트 리셋
                    break                                 # i for문으로 탈출
                    
        return longest