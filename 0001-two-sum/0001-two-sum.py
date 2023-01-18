class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resultList = []
        for i in range(0,len(nums)-1) :
            for j in range(i+1,len(nums)) :
                first = nums[i]
                second = nums[j]
                if first + second == target :
                    resultList.append(i)
                    resultList.append(j)
                    return resultList

