class Solution:
    def isHappy(self, n: int) -> bool:
        # 2 : -> 4 -> 15 -> 37 -> 30 -> 9 -> 81 -> 65 -> 61 -> 37
        # 37이 두번나옴 : 사이클이 발생하므로 절대 1, 즉 행복한 수가 될 수 없다
        
        # 방문한 적이 있는지 체크 , 파이썬의 set자료형은 중복을 허용하지 않음을 이용
        visit = set() 
        
        # visit에 있던 원소가 또 나오면 while조건을 만족하지 않으므로 자연적으로 탈출
        while n not in visit:
            # n 이 visit안에 원소가 아니라면 새로 추가해줌 add()
            visit.add(n)
            n = self.sum_square(n)
            
            if n == 1 :
                return True
        
        # while에서 빠져나오게 되면
        return False
    
    
    # 각 자리수의 제곱의 합을 구하는 함수를 따로 정의하는 것이 가독성에 좋다.
    def sum_square(self, n: int) -> int:
        res = 0 
        
        # n이 0 이 아닐시 계속 반복 , 0 일시 while 탈출
        while n :
            # 10을 나눈 나머지 -> 1의 자리수
            # 제곱하여 합에 더함
            digit = n % 10
            digit = digit ** 2
            res += digit
            
            # 그 후 몇의 자리 까지 있을지 모르지만 한자리씩 올라가며 반복
            # 몫이 0 이 될시 탈출
            n = n // 10
            
        return res