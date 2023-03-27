class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # count(val) 메소드는 해당 리스트 안에 val이 몇개 있는지 세어준다. 
        # val 이 리스트 안에 있으면 반복
        while nums.count(val):
            # remove(val) 메소드는 해당 리스트 안의 val값을 삭제한다.
            nums.remove(val)
        
        return len(nums)