class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            # 이미 딕셔너리에 있는 키 일경우 값에 2(2번이상은 모두 2로 표시되므로 0으로 하든 -1 로 하든 상관없음)
            if num in counter.keys():
                counter[num] = 2
            # 처음 나온경우 키값에 1
            else:
                counter[num] = 1
        
        # 딕셔너리 값들중 값이 1인 키를 출력
        for key, value in counter.items():
            if value == 1:
                return key
            
            
'''
^ XOR을 사용한 풀이
이전과 같
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer = answer ^ num
        return answer
'''