'''
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
'''
# 위의 풀이는 for문 2개로 너무느림
# 슬라이딩 윈도우 개념을 사용하여 for문 하나로 시간복잡도 단축
    
class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()              # 파이썬 set은 반복을 허용하지 않음. 같은 문자열이 나오는지 체크하는 용도
        l = 0
        result = 0

        for r in range(len(s)):     # r 포인터는 문자열 길이만큼 순회한다
            while s[r] in window:   # 중복되는 문자가 있으면 
                window.remove(s[l]) # 중복되는 문자가 없을때 까지 
                l += 1              # l 포인터를 늘리면서 지워줌
            window.add(s[r])        # 그 다음 현위치의 문자를 삽입 
            result = max(result, r - l + 1)

        return result

'''
ex) abcba 일때
l = 0 , r = 2 , result = 3
window = (a,b,c)
l = 0 , r = 3  -> s[r] 이 b 인데 이미 set안에 있음 
s[l = 0] 즉 a 삭제 window = (b,c)  l += 1
s[l = 1] 즉 b 삭제 window = (c)

이제 b와 겹치는 값이 set에 없음 
다시 b 삽입 window = (c,b)
r-l+1 = 2 이전의 result = 3 보다 작으므로 갱신 X 
'''