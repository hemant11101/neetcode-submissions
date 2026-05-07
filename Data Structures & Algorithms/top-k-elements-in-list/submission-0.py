class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dickt = {}
        for i in nums:
            dickt[i] = 1 + dickt.get(i,0)
        arr = []
        for i , j in dickt.items():
            arr.append([j,i])
        arr.sort()
        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res
        
