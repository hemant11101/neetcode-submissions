class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        k = 0
        j = len(nums)
        for i in range(len(nums)):
            ans.append(nums[i])
        for j in range(j,2*j):
            ans.append(nums[k])
            k += 1
        return ans


        
