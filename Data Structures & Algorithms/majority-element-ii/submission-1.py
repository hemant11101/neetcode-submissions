class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        bench = len(nums)/3
        res = []
        countdict = defaultdict(int)
        for i in nums:
            countdict[i] += 1
        for i, k in countdict.items():
            if k > bench:
                res.append(i)
        return res
