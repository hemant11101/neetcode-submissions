class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        mapQuad = defaultdict(int)
        nums.sort()
        for i in nums:
            mapQuad[i] += 1

        for i in range(len(nums)):
            mapQuad[nums[i]] -= 1

            if i>0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)):
                mapQuad[nums[j]] -= 1

                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                
                for k in range(j+1, len(nums)):
                    mapQuad[nums[k]] -= 1

                    if k>j+1 and nums[k] == nums[k-1]:
                        continue
                    
                    remSum = target - (nums[i]+nums[j]+nums[k])
                    if mapQuad[remSum]>0:
                        res.append([nums[i],nums[j],nums[k],remSum])
                for k in range(j+1,len(nums)):
                    mapQuad[nums[k]] += 1
            
            for j in range(i+1,len(nums)):
                    mapQuad[nums[j]] += 1
            

        return res          



        