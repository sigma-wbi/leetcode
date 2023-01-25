class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[-1] < target:        # target값이 nums안의 모든 값보다 크면
            return len(nums)        # target이 들어갈 위치는 가장 마지막
        else:
            for i,elem in enumerate(nums) :
                if elem < target:       # target이 있을 위치를 찾는과정 오른쪽으로 한칸씩 이동
                    continue
                else :                  # target값과 똑같은 값을 찾거나 target값을 넘어버리면
                    return i