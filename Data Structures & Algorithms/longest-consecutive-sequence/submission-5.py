class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mapArray = set(nums)
        maxC = 0
        if not nums:
            return 0
        if len(nums)== 1:
            return 1
        for i in mapArray:
            if i - 1 not in mapArray:
                curr = i
                count = 1
                while curr + 1 in mapArray:
                    curr += 1
                    count += 1
                maxC = max(count, maxC)
        return max(maxC, 1)