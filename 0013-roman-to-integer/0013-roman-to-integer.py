class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I': 1,'V': 5,'X': 10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        s = s[::-1]             #빼기 연산을 편하게 하기 위해 받은 문자열을 뒤집는다 for문 돌릴때 역순으로 돌려도 되긴함
        print(s)
        for i in range(len(s)):
            if i == 0:          #첫번째는 그냥 더하기 i-1인덱스가 없으므로
                res += dic[s[i]]
            else:
                if dic[s[i]] < dic[s[i-1]] :        # 뒤집은 현재 문자열이 이전 문자열보다 작으면 지금꺼는 합에서 뺀다
                    res -= dic[s[i]]
                else :
                    res += dic[s[i]]

        return res