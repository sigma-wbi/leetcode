# for 문 2개로 부르트포스로 풀면 런타임 오류 (O(n2))
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        
        # 최솟값과 최댓값(profit)을 계속 갱신
        # 현 위치의 값에서 최솟값을 뺀값을 profit과 비교
        # [7,1,5,3,6,4] 일경우 7, 1 까지는 min이 7, 1 
        # 그리고 prifit 은 0 
        # 5에서 부터 min 값이 1에서 갱신되지 않으므로 5-1 = 4 , profit = 4
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        
        return profit