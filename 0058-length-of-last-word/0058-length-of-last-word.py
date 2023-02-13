class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 맨 끝에 공백이 있을 경우 일단 제거 (제거 안하면 마지막 단어 길이가 0으로 나오므로)
        rstrip_s = s.rstrip()
        li = []
        for i in range(len(rstrip_s)-1,-1,-1):
            li.append(rstrip_s[i])
        print(li)
        # 맨 끝 공백을 제거했으면 단어 중간 공백이 나올때 까지 마지막 단어 길이를 셈
        giri = 0
        for elem in li :
            if elem == ' ':
                break
            giri += 1
        
        return giri