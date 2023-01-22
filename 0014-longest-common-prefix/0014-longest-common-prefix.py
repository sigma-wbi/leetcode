class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:      #문자열 리스트가 1개 밖에 없으면
            return strs[0]       #그 하나 문자열 전체가 prefix
        
        # 1개 이상일시
        strs.sort(key=len)      #길이 기준으로 정렬한다, 제일 짧은 문자열이 맨앞(strs[0])
        res =""
        
        for i in range(len(strs[0])):   # 첫번째 문자열의 모든 문자를 순회
            find = strs[0][i]   # 비교 대상이되는 첫번째 문자열의 i 문자
            for j in range(1,len(strs)):# 제일 짧은 문자열 strs[0] 말고 모든 문자열 체크
                if find == strs[j][i]:   # 비교대상이 같으면
                    if j == len(strs) - 1:  # 또한 마지막 문자열일경우 (모든 문자열 비교가 끝났을경우)
                        res += find
                else :                  # 비교중에 다른경우가 나오면 뒤에는 순회할 필요없음
                    return res
                    
        return res
                