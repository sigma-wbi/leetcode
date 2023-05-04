'''
#런타임 오류
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n == 1) or ( n == 2 ) :
            return True
        
        # 음수일 경우 양수로 변환(어차피 똑같음)
        if n < 0 :
            n = -n
            
        while (n % 2 == 0):
            # 나머지가 1일시 False
            if n % 2 == 1 :
                return False
            
            # 나머지가 0일시 다음  루프 2로 나눈 몫으로
            n /= 2
            # 2로 나눴을떄 몫이 2면 끝
            if n == 2:
                return True
            
        return False
    
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        answer = False
        pow_2s = []
        
        for i in range(50):
            pow_2s.append(pow(2, i))
            
        if n in pow_2s:
            answer = True
            
        return answer
'''

#비트로 풀이 
# ex) 8 -> 2진수 1000
# 8-1 = 7 -> 2진수 0111 
# &연산하면 0
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n & (n-1)==0