class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if nums[i]>nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        return nums

                            