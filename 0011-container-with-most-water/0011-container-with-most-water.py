'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        for i in range(len(height)-1):
            for j in range(i+1,len(height)):
                h = min(height[i],height[j])
                w = j - i
                area = h*w
                if area > maxA :
                    maxA = area

        return maxA
O(N2) -> 런타임 에러 O(N) 으로 개선 필요
 '''   
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        #양 끝을 포인터로 둔다
        left=0
        right=len(height)-1
        max_area=0
        while (right-left>0) :      # 양끝이 유효할때까지 반복 (반복문 1개 -> O(N))
            # 현재 두포인터 기준으로 물의 양과 max값과 비교
            max_area=max(max_area,(right-left)*min(height[left],height[right]))     
            
            # 포인터를 동시에 땡겨서는 안됨, 경우에 따라서 한개씩 땡김
            if height[left]>=height[right]: # 오른쪽 포인터의 높이가 왼쪽보다 작으면 
                right-=1                    # 오른쪽 포인터 왼쪽으로 땡김 (더 짧은 포인터를 땡겨와서 최신화 시켜야 물의양이 늘어날 가능성이 있음)
            else: 
                left+=1
            
        return max_area