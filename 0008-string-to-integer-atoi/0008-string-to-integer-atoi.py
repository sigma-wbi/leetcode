class Solution:
    def myAtoi(self, s: str) -> int:
        intS = []                           # 숫자인 원소만 담을 리스트 선언
        # 숫자의 최대와 최소 범위
        maxInt = 2**31 -1
        minInt = -(2**31)
        
        # 입력값이 없으면 0으로 처리
        if s == '' :
            return 0
        
        # 선행 공백 판별
        while s[0] == ' ':
            s = s[1:]
            # 문자열이 전부 공백일경우 (공백 다 뺐을때 문자열이 없으면)
            if len(s) == 0 :
                return 0
            
        # 부호 판별
        a = True                            # 양수를 true로 표현하고 이를 기본값으로 한다.(부호표시가 없을경우도 양수)
        if s[0] == '-':
            a = False                       # 음수 부호가 있을 경우는 false로 음수임을 표시 
            s = s[1:]
        elif s[0] == '+':
            a = True                        # 양수 부호가 있을 경우는 true로 양수임을 표시 
            s = s[1:]
        
        # 숫자 판별
        b = True
        try :
            int(s[0])
        except :    
            b = False
        # 공백, 부호 제거후 다음 문자열이 숫자가 아니면 볼필요없이 0으로 반환
        if b == False:
            return 0
        
        for elem in s :
            try :
                intS.append(int(elem))      # int로 형변환이 되는 원소는 숫자 리스트 안에 담고
            except :    
                break                       # 형변환때 에러가 발생할시 거기까지.(문자열 원소인경우)
            
        # 선행 0 제거
        while intS[0] == 0:                 # 리스트의 맨앞 원소가 0이 아닐때까지 맨앞의 0을 제거
            intS = intS[1:]
            # 담긴 숫자가 전부 0일경우 (0 다 뺐을때 문자열이 없으면)
            if len(intS) == 0 :
                return 0
        
        # 결과 도출
        newS = ""                           # 리스트 안의 원소를 문자열로 바꾸기 위함
        for elem in intS :
            newS += str(elem)
            
        if a == True:                       # 양수이면 양수로 음수이면 음수로 
            result = int(newS)
        else :
            result = -(int(newS))
        
        if result > maxInt :
            result = maxInt
        if result < minInt :
            result = minInt  
            
             
        return result

'''
isdigit() 함수를 사용한 풀이
class Solution:
    def myAtoi(self, s: str) -> int:
        index = 0
        sign = 1
        upper_bound = 2 ** 31 - 1
        lower_bound = -(2 ** 31)
        result = 0

        # condition 1 -> ignore any whitespace
        while index < len(s) and s[index] == ' ':
            index += 1
        
        # condition 2 -> check whether next char is plus or minus
        if index < len(s) and s[index] == '-':
            sign = -1
            index += 1
        elif index < len(s) and s[index] == '+':
            index += 1
        
        # condition 3 -> read in until non-digit is found
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1

        result = result * sign

        # condition 4 -> check if the result is within 32-bit signed range.
        if result < lower_bound:
            return lower_bound
        if result > upper_bound:
            return upper_bound

        return result
'''