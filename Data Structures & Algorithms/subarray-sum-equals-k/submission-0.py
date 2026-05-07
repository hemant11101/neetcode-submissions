class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        countK = {0: 1}
        current_sum = 0
        count = 0
        for i in nums:
            current_sum += i
            if (current_sum - k) in countK:
                count += countK[current_sum - k]
            countK[current_sum] = countK.get(current_sum, 0) + 1
        return count