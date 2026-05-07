class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j = len(numbers)-1
        i = 0 
        res = []
        while j>i :
            s = numbers[i]+numbers[j] 
            if  s == target:
                return [i+1,j+1]
            elif s > target:
                j -= 1
            else:
                i += 1
      
        

                        
        