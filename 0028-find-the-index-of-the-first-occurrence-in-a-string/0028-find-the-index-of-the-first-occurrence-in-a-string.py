class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # haystack 의 길이가 더 길다. 
        
        for i in range(len(haystack)-len(needle)+1):
            # 문자열 슬라이싱 활용
            if haystack[i:i+len(needle)]==needle:
                # 조건을 만족하면 시작 위치 반환
                return i
        
        return -1