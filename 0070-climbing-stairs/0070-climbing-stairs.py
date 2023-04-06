# 동적계획법 -> 점화식 생성, 초기값 설정, 반복문을 통해 배열에 기록

class Solution:
    def climbStairs(self, n: int) -> int:
        # n=3 일때의 가짓수를 차례차례 저장하기 위한 배열, n이 0,1,2 일때를 처리하기 위해 F(0),F(1),F(2)를 미리 초기화
        dp_array = [0,1,2]
        if n < len(dp_array):
            # 0,1,2 일경우 그대로 0,1,2 qksghks
            return dp_array[n]

        # 3이상일시 점화식 F(n) =  F(n-1) + F(n-2)
        # 어떤 계단을 오르기 위한 방법은 한칸전에서 오르는 방법과 두칸전에서 오르는 방법의 합
        for i in range(3, n+1):
            ith_way = dp_array[i-1] + dp_array[i-2]
            # F(3)부터 차례로 배열에 저장
            dp_array.append(ith_way)

        return dp_array[n]