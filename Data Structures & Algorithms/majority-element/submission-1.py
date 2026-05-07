class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = majCount = 0
        countDict = defaultdict(int)

        for num in nums: 
            countDict[num] += 1
            majcount = countDict[num]
            if majcount>res:
                res = majcount
                toret = num

        return toret
        