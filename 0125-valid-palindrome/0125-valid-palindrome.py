class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 빈 문자열일시 True 반환
        if s == " ":
            return True
        
        # 파이썬의 다양한 내장 함수를 통해 주어진 조건 만족
        # 1 s.lower() : 문자열 s를 소문자로 변환한다
        # 2 s.replace(a,b) : 문자열 s안에 a가 있으면 모두 b로 치환한다
        # 3 s.isalpha() : 문자열 s안에 문자중 알파벳만 출력한다
        '''
        res = s.lower()
        res = res.replace(" ","")
        res = [i for i in res if i.isalpha()]
        # 리스트 컴프리헨션을 리스틀 만든것을 문자열로 변환
        res = ''.join(res)
        '''
        
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        
        # 조건을 만족시킨 문자열과 이를 뒤집은 문자열이 같은지 비교
        return s==s[::-1]
                      