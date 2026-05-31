class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        mapNums = defaultdict(int)
        for i in range(0,len(nums)):
            mapNums[nums[i]] += 1
        for i in range(len(nums)):
            mapNums[nums[i]] -= 1
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            
            for j in range(i+1,len(nums)):
                mapNums[nums[j]] -= 1
                if j-1> i and nums[j] == nums[j-1]:
                    continue
                
                twoSum = nums[i]+nums[j]
                reqSum = -twoSum
                if mapNums[reqSum] > 0:
                    res.append([nums[i], nums[j], reqSum])
            for j in range(i+1, len(nums)):
                mapNums[nums[j]] += 1
        return res
                
                  



            
        