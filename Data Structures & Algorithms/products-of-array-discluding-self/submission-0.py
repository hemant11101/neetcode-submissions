from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prod = 1
        zero_count = nums.count(0)

        # If more than one zero, all products will be zero
        if zero_count > 1:
            return [0] * len(nums)
        
        # Calculate the product of all non-zero elements
        for i in nums:
            if i != 0:
                prod *= i
        
        for i in nums:
            if zero_count == 0:
                res.append(prod // i)
            else:
                # Only the position with zero gets the product, others get zero
                res.append(prod if i == 0 else 0)
        return res
