class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = list(set(nums))      #set으로 중복삭제
        temp.sort()                 #리스트 정렬
        for i, v in enumerate(temp):
            nums[i] = v             #임시리스트 값을 원본 nums에 삽입
        
        return len(temp)
        