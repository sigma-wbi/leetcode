class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = set()      # 중복된 결과값을 도출하지 않기위해 set()사용
        nums.sort()
        
        # 포인터 4개를 사용하기위함 i, j , left, right 의 합을 sum으로 한다.
        # 순서는 j ,i ,left, right 순 
        for j in range(len(nums) - 3):
            for i in range(j+1, len(nums) - 2):
                left = i + 1
                right = len(nums) - 1
                
                # 투 포인터 
                while left < right:
                    sum = nums[j] + nums[i] + nums[left] + nums[right]
                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        # 결과를 담을 곳이 중복을 막을 set()을 사용하였으므로 
                        # append 대신 add를 사용해야함
                        result.add((nums[j], nums[i], nums[left], nums[right]))
            
                        # 중복제거
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1

        return result