class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i,j = 0, len(people)-1
        count = 0 
        sum = 0
        people.sort()
        while(i<=j):
            sum = people[i]+people[j]
            if sum>limit:
                count+=1
                j-=1
            elif i==j :
                count +=1
                i+=1
            else :
                count+= 1
                i+=1
                j-=1
            
        return count

