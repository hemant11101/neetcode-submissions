class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        def reversefunc(i:int , j:int)-> None:
            while(i<j):
                nums[i] , nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        reversefunc(0, n-1)
        reversefunc(0, k-1)
        reversefunc(k, n-1)






        